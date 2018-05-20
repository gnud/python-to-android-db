from django.test import TestCase
import contextlib
from io import StringIO

# Create your tests here.


def capture_stdout(obj):
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        obj()
    output = temp_stdout.getvalue().strip()
    return output


class TestTask1(TestCase):
    def setUp(self):
        pass
