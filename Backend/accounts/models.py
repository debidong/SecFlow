# from django.contrib.auth.models import AbstractUser
from django.db import models
from hashlib import md5
import random
import string
# from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    uid = models.CharField(unique=True, max_length=20)
    salt = models.CharField(max_length=32)
    friend = models.ManyToManyField('self', symmetrical=False)

    # Set MD5(password + salt) as password
    def set_password(self, password):
        # generate random string for salt
        letters = string.ascii_letters
        self.salt = ''.join(random.choice(letters) for i in range(32))
        hash_digest = md5(str(password + self.salt).encode('utf-8')).hexdigest()
        self.password = hash_digest

    @staticmethod
    def exists(uid) -> bool:
        if not User.objects.filter(uid=uid).exists():
            return False
        else:
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
