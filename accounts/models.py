from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
"""
class progile
bio
profile_image
address
user
"""
class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.URLField(max_length=500, blank=True)
    address = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"{self.user.username}'s Profile"