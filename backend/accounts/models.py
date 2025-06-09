from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    signup_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
