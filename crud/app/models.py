from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.IntegerField()
    DOB = models.DateField()
    password = models.CharField(max_length=500)