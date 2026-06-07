from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField
# Create your models here.
class User(AbstractUser):
    email = EmailField(unique=True, max_length=254)
    username = CharField(max_length=150, unique=True, blank=True, null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []