# from django.contrib.auth.models import AbstractUser
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

    @staticmethod
    def check_user_exists(uid) -> bool:
        user = User.objects.all().filter(uid=uid)
        if not user.exists():
            return False
        return True

    @staticmethod
    def check_password(uid, password):
        if not User.check_user_exists(uid):
            return False
        user = User.objects.all().filter(uid=uid)
        # _password = user.get('password')
        try:
            # if password == _password:
            if user.filter(password=password).exists():
                return True
            else:
                return False
        except:
            return False