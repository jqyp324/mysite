from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=26)
    members = models.ManyToManyField('Person')

    def __str__(self):
        return self.name
