from django.db import models
from django.contrib.auth.models import AbstractUser
# from djongo import models

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"id {self.id}, {self.first_name}"

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'



