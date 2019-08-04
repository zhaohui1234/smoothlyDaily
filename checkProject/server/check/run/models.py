from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    wx_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now=True)
    

class Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    
    seq = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=100)
