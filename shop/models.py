from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def is_underage(self):
        return timezone.now().year - self.birth_date.year < 18

    def __str__(self):
        return self.name


class Bicycle(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    to_fix = models.CharField(max_length=20)

    def __str__(self):
        return self.name
