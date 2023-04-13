from django.db import models


# User is used by Django, so we have to find another name for the class
# this is a custom model
class UserAccount(models.Model):
    username = models.CharField(max_length=22, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=22)
    signup_time = models.DateTimeField(auto_now=True)

