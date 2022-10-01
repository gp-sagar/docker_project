from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=55)