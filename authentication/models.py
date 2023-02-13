from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
import uuid


class UserManager(BaseUserManager):
    def create_user(self, username, firstname, lastname, password=None):
        user = self.model(username=username,
                          firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, firstname, lastname, password=None):
        user = self.model(username=username,
                          firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.is_verified = True
        user.save()
        return user


class User(AbstractBaseUser):
    public_key = models.UUIDField(
        default=uuid.uuid4, editable=False, null=False, unique=True)
    username = models.CharField(max_length=50, null=False, unique=True)
    fisrtname = models.CharField(max_length=150, null=False, unique=False)
    lastname = models.CharField(max_length=150, null=False, unique=False)
    email = models.EmailField(max_length=10, null=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
