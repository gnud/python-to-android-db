# noinspection PyUnresolvedReferences
# We define models for in Android in this module, since we like to make models.py a generic file for any project
from django.conf import settings

from .mymodels import *


# Write your tools models here
class SampleTest(models.Model):
    """
    Only for unit testing
    """

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False, )
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    name = models.CharField(max_length=1000)
