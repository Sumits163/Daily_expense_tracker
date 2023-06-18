from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=25)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField(200)
    password = models.CharField(max_length=256)
    
