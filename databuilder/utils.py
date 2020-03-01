import glob
import os
from django.conf import settings
from dbbackup.db.base import get_connector
from databuilder import models


def cleanup():
    """
    Performs dump cleanup
    """

    # Remove old dump files, just in case
    [os.remove(f) for f in glob.glob(settings.DUMPS_DIR_DUMP_REG)]


def check_exclude(item):
    """
    Matches the django related tables and excludes the DDL lines

    :type item: str
    :param item Contains DDL sql query command
    :return:
    """
    excluded_tables = ['django_', 'auth_']

    if not settings.TESTING:
        # TODO: this is retarded approach, find better solution
        # The goal was to have basic testing models, but that failed
        sample_model_name = f'{models.SampleTest.__name__.lower()}'
        excluded_tables.append(sample_model_name)

    has_excluded = any([True for i in excluded_tables if i in item])
    return True if not has_excluded else False


def locate_sql_dump():
    """
    Locate the last sql dump as file path
    @:rtype str
    """

    full_path_regex = os.path.join(settings.DUMPS_DIR, settings.DUMP_REG)
    dump_file = next(iter(glob.glob(full_path_regex)), None)
    has_existing_file = os.path.exists(dump_file)
    assert has_existing_file

    return dump_file


def generate_file():
    """
    Copied from the library: package dbbackup and module dbbackup/management/commands/dbbackup.py
    TODO: either rewrite it, or suffer the consequences :D.
    """

    return get_connector('default').generate_filename()


def without_django_tables(data):
    """
    Exclude any django related table

    :type data: List
    :return:
    """
    return [dc for dc in data if check_exclude(dc)]


def fix_names(target, data):
    """
    TODO: maybe will be slow if too many records, but on the other hand
    why do you pack 1tb data on your Android device :D!!!
    :param target: The content to match
    :type target: str
    :type data: List
    :rtype: List
    """
    return [i.replace(f'{target}_', '') for i in data]
