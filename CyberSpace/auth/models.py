from django.db import models
# from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=16)
    uid = models.CharField(unique=True, max_length=20)
