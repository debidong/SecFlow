# from django.contrib.auth.models import AbstractUser
from django.db import models
from hashlib import md5
import random
import string
# from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    uid = models.CharField(unique=True, max_length=20)
    salt = models.CharField(max_length=32)
    friend = models.ManyToManyField('self', symmetrical=False)

    def set_user_info(self, username, password, uid):
        self.username = username
        self.uid = uid

        # generate random string for salt
        letters = string.ascii_letters
        self.salt = ''.join(random.choice(letters) for i in range(32))
        hash_digest = md5(str(password + self.salt).encode('utf-8')).hexdigest()
        self.password = hash_digest

    @staticmethod
    def check_user_exists(uid) -> bool:
        user = User.objects.all().filter(uid=uid)
        if not user.exists():
            return False
        return True

    @staticmethod
    def check_password(uid, password):
        user = User.objects.all().get(uid=uid)
        try:
            password = md5((password + user.salt).encode('utf-8')).hexdigest()
            if user.password == password:
                return True
            else:
                return False
        except:
            return False
