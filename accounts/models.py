from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True
User._meta.get_field('email')._null = False

class UserAuthentication(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    device_token = models.TextField(blank=True)
