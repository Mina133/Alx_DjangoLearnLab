from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)

    groups = None
    user_permissions =  models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Provide a unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    def __str__(self):
        return self.username