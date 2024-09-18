from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.custom_usermanager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=256, unique=True)
    objects = UserManager()

    def __str__(self):
        return str(self.email)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []