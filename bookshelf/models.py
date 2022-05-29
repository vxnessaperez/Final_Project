from collections import UserDict
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
User.is_staff = False
User.is_active = True
User.is_superuser = False