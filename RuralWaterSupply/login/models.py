from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Village_ID = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    Type = models.CharField(max_length = 50) 
    def __str__(self):
        return self.username
