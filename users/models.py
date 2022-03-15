from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    img_profile = models.ImageField(null=True, blank=True)

