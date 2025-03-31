from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    
    uid = models.UUIDField(default=None, blank=True, null=True, unique=True)
    
    USERNAME_FIELD = 'uid'
    email = models.CharField(max_length=30, default=None)
    username = models.CharField(max_length=30, default=None)