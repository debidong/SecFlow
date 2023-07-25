from django.db import models
from accounts.models import User

# Create your models here.

class Room(models.Model):
    rid = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(to=User, blank=True)

    def join(self, user):
        self.users.add(user)
        self.save()

    def leave(self, user):
        self.users.remove(user)
        self.save()

    def __str__(self):
        pass

class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def get_msg(self):
        return {
            'user': self.user.username,
            'rid': self.room.rid,
            'content': self.content,
            'time': self.time
        }