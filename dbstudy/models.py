from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=26)
    members = models.ManyToManyField('Person')

    def __str__(self):
        return self.name
