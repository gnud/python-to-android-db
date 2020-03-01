import os
import sqlvalidator

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

from databuilder import utils
from databuilder import apps


class Command(BaseCommand):
    # noinspection SpellCheckingInspection
    """
        Usage:
        ./manage.py toandroid

        SQL dump of the models defined in models.py
        """

    help = 'Dumps SQL of the django structure for Android SQLite, excluding django related tables/'

    def handle(self, *args, **options):
        self.setup()
        self.do_backup()
        ddl_commands = self.extract_user_tables()
        print(*ddl_commands)
        utils.cleanup()

    def add_arguments(self, parser):
        """
        TODO:
        argument to allow file output, for instance Android project path
        argument to execute some command, e.g: call  gradle build task
        """
        pass

    @staticmethod
    def setup():
        """
        Clean and migrate stuff
        """
        utils.cleanup()

        # noinspection SpellCheckingInspection
        call_command('makemigrations', 'databuilder', verbosity=0)
        # noinspection SpellCheckingInspection
        call_command('migrate', 'databuilder', verbosity=0)

    @staticmethod
    def extract_user_tables():
        # noinspection SpellCheckingInspection
        """
                Extract user created model tables defined in models.py.

                 @:rtype List
                """

        dump_file = utils.locate_sql_dump()

        # Open the sql dump and read it as list
        ddl_data = open(dump_file, 'r').readlines()

        assert len(ddl_data), 'Try running:\n./manage migrate'

        ddl_data_clean = utils.fix_names(
            apps.DatabuilderConfig.name,
            utils.without_django_tables(ddl_data),
        )

        # noinspection SpellCheckingInspection
        assert len(ddl_data_clean), 'Try adding some models in models.py\n then run:\n./manage migrate'

        # Confirm each line for valid SQL query line
        result = any([sqlvalidator.parse(cmd).is_valid() for cmd in ddl_data_clean])

        assert result, 'Some ddl command line is invalid, maybe the tool need upgrade, file an issue at project REPO'

        return ddl_data_clean

    @staticmethod
    def do_backup():
        """
        Performs the backend command that does the actual SQL dump
        """

        _dumps_dir = settings.DUMPS_DIR
        _file = utils.generate_file().replace('.dump', '.sql')
        full_path = os.path.join(_dumps_dir, _file)

        # noinspection SpellCheckingInspection
        call_command('dbbackup', '-O', full_path, verbosity=0)
