from django.db import models
from Login.models import User

# Reminder for Reminder module.
class Reminder(models.Model):
    topic = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Friend Request for Friend module.
class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')