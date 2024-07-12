from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    pass

class Interest(models.Model):
    sender = models.ForeignKey(Users, related_name='sent_interests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name='received_interests', on_delete=models.CASCADE)
    accepted = models.BooleanField(null=True, default=None)  # None = pending, True = accepted, False = rejected

class Message(models.Model):
    sender = models.ForeignKey(Users, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)