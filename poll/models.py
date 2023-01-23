from django.db import models
# Create your models here.
from datetime import datetime

class polldata(models.Model):
    question = models.CharField(max_length=500)
    option_one = models.CharField(max_length=20)
    option_two = models.CharField(max_length=20)
    option_three=models.CharField(max_length=20)
    option_four=models.CharField(max_length=20,default=None)
    option_one_count=models.IntegerField(default=0)
    option_two_count=models.IntegerField(default=0)
    option_three_count=models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)
    users = models.TextField()
    userid=models.IntegerField(default=0)
    time=models.CharField(max_length=20,default=None)

def total(self):
    return option_one_count+option_two_count+option_three_count