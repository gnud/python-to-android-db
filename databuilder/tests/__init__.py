from django.test import TestCase
from django.core.management import call_command

from databuilder.tests import utils
from databuilder import models

# noinspection SpellCheckingInspection
sample_name = 'Bob Bobski'


class TestTask1(TestCase):
    def setUp(self):
        self.model_name = models.ContactSample.__name__.lower()

        models.ContactSample.objects.create(name=sample_name)

    def test_dump(self):
        total_records = models.ContactSample.objects.all().count()
        print(f'Your model has {total_records} dummy record.')

        # noinspection SpellCheckingInspection
        with utils.capture(call_command, 'toandroid') as output:
            self.assertIn(self.model_name, output)   # CREATE Table statement
            self.assertIn(sample_name, output)  # INSERT Statement
