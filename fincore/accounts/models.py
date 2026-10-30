from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    role=models.CharField(
                          max_length=50, 
                          choices=[
                              ('Customer', 'Customer'),
                              ('Bank Employee','Bank Employee'),
                              ('Insurance Agent','Insurance Agent')
                              ,('Admin', 'Admin')], 
                              default='Customer'
                            )

