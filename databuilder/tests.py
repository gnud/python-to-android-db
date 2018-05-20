from django.test import TestCase
import contextlib
from io import StringIO
import unittest

# Create your tests here.


def capture_stdout(obj):
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        obj()
    output = temp_stdout.getvalue().strip()
    return output


class TestTask1(unittest.TestCase):
    def setUp(self):
        self.board = app.Board()

    def test_destroyer(self):
       pass