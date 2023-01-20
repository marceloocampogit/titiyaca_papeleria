from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=12, null=True)
    birthday = models.DateField(null=True)
    photo = models.ImageField(upload_to='profile_images', null=True, blank=True)