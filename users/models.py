from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image',blank=True, null=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True, null= True)

    def __str__(self):
        return self.username