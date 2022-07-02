from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
User.is_staff = False
User.is_active = True
User.is_superuser = False

class Review(models.Model):
    book_title = models.CharField(max_length=500, default='')
    author_name = models.CharField(max_length=500, default='')
    review = models.CharField(max_length=500, default='')

    def __str__(self):
        return f"{self.book_title}"