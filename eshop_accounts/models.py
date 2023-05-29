
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_writer=models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت ها'