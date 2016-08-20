"""User model."""
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """User profile."""

    user = models.OneToOneField(User, unique=True)
    location = models.TextField()
    register_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now)


class Products(models.Model):
    """Product of user."""

    user = models.ForeignKey(UserProfile)
    name = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField()
    amount = models.IntegerField()
    required_hour = models.FloatField()
    likes = models.IntegerField()
    pictures = models.TextField()
    pub_date = models.DateTimeField('date published')
    update_date = models.DateTimeField('date updated')


class History(models.Model):
    user = models.ForeignKey(UserProfile)
    p_id = models.IntegerField()
    created = models.DateTimeField()
