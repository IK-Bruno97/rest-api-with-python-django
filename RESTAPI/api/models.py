from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_of_birth = models.CharField(max_length=100)

