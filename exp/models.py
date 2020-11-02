from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your 

class Users(AbstractUser):
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.IntegerField()

class user_model(models.Model):
    Name=models.CharField(max_length=100,blank=True)
    Image=models.ImageField(upload_to='exp/static',blank=True)
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)

    
    class Meta:
        abstract=False

    def __str__(self):
        return self.Username



class newusers(user_model):
    gender=models.CharField(max_length=10)


class new1(user_model):
    age=models.FloatField()

class record(models.Model):
    Date=models.DateField(blank=True,null=True)
    Description=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Amount=models.IntegerField()
    User=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Description