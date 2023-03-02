from operator import mod
from turtle import mode
from django.db import models
class Temp(models.Model):
    template = models.FileField(upload_to='')
class Mail(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    inquiry = models.CharField(max_length=70)
    message = models.CharField(max_length=170)

class Att(models.Model):
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=100)
    attach = models.FileField(upload_to='')
    message = models.CharField(max_length=120)
class Upld(models.Model):
    # id = models.BigIntegerField(primary_key=True, max_length=20)
    name = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, null=True)
    inquiry = models.CharField(max_length=70, null=True)
    message = models.CharField(max_length=170, null=True)
    # file = models.FileField(upload_to="media", null=True, blank=True)
