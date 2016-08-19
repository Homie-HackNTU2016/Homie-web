from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    admin = models.BooleanField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.TextField()
    register_date = models.DateTimeField('date registered')
    updated_date = models.DateTimeField('date updated')


class Products(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE())
    name = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField()
    amount = models.IntegerField()
    required_hour = models.FloatField()
    likes = models.IntegerField()
    pictures = models.TextField()
    pub_date = models.DateTimeField('date published')
    update_date = models.DateTimeField('date updated')
