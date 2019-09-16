import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateTimeField('birth date')

    def is_underage(self):
        return timezone.now().year - self.birth_date.year < 18

    def __str__(self):
        return self.name

class Bicycle(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
