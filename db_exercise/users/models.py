from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)

    # def __init__(fn,ln,em):
    #     first_name = fn
    #     last_name = ln
    #     email = em
