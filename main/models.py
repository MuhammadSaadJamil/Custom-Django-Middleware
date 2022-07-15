from django.db import models


# Create your models here.

class Object(models.Model):
    name = models.CharField(max_length=25)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
