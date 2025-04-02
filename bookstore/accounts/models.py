from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.


# Sin hacer esto daba error "AttributeError at /accounts/login/'Manager' object has no attribute 'get_by_natural_key'"
class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class CustomUser(AbstractBaseUser):
    objects = CustomUserManager() # Lo mismo que el comentario de arriba
    
    uid = models.UUIDField(default=None, blank=True, null=True, unique=True)
    
    USERNAME_FIELD = 'uid'
    email = models.CharField(max_length=30, default=None)
    username = models.CharField(max_length=30, default=None)
    
