from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()


class Manufacturer(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    pass


class ModelType(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Bicycle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    model_type = models.ForeignKey(
        ModelType, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
