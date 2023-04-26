from django.db import models


# User is used by Django, so we have to find another name for the class
# this is a custom model
class UserAccount(models.Model):
    username = models.CharField(max_length=22, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=22)
    signup_time = models.DateTimeField(auto_now=True)

class CustomMessage(models.Model):
    my_email = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    my_msg = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.my_email
    
class ChatBox(models.Model):
    messenger = models.CharField(max_length=50, blank=True)
    message = models.TextField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.messenger