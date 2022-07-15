from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)

    def __str__(self):
        return self.name
