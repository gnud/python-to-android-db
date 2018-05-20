import glob
import os
import sys
import time

from django.conf import settings


location_name = sys.argv[2].split('=')[1] if len(sys.argv) >= 2 and 'location' in next(iter(sys.argv[2:]),
                                                                                       'False') else None


def prepare_new_db():
    try:
        allow_command('buildbase')

        db_name = '%s' % (time.strftime("%Y%m%d-%H%M%S"))
        switch_default_db(location_name, db_name)
    except:
        pass


def switch_default_db(location_name="db", db_name="", fpath=False):
    if not fpath:
        fulldb_name = 'db_%s_%s.sqlite3' % (location_name, db_name)
    else:
        fulldb_name = location_name

    databases = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, fulldb_name),
        }
    }

    settings.DATABASES = databases


def prepare_for_dump():
    try:
        allow_command('dumpsql')

        databases = glob.glob('*%s*.sqlite3' % location_name)

        if len(databases) == 0:
            print('Please generate a database first: ./manage.py buildbase --location=%s' % location_name)
            sys.exit(1)
            return

        value = ask_db(databases)

        switch_default_db(location_name=value, fpath=True)
    except Exception as e:
        pass


# region Helpers
def allow_command(cmd):
    if cmd not in sys.argv[1]:
        raise Exception()


def ask_db(databases):
    choices = dict(zip(range(0, len(databases)), databases))

    if len(choices) == 1:
        return choices[0]

    input_msg = 'Choose item from the list:\n'
    answer = None
    for k, v in choices.items():
        print('%s. %s' % (k, v))
    try:
        answer = int(input(input_msg))
    except:
        pass
    while answer not in choices.keys():
        try:
            answer = int(input(input_msg))
        except:
            pass
    else:
        value = choices[answer]

    return value


# endregion

prepare_new_db()
prepare_for_dump()
