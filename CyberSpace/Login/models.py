from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=20)
    uid = models.CharField(unique=True, max_length=20)

    def set_user_info(self, username, password, uid):
        self.username = username
        self.password = password
        self.uid = uid