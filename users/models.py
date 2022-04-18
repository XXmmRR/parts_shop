from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    Full_name = models.CharField(max_length=200, verbose_name='ФИО')
    phone = models.CharField(max_length=16, blank=False, verbose_name='Телефон')
    address = models.CharField(max_length=200, verbose_name='Адрес')
