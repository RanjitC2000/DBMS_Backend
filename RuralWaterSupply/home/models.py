from django.db import models

# Create your models here.
class BigProject(models.Model):
    Development = models.CharField(max_length=100,primary_key = True)
    Funds = models.IntegerField()
    def __str__(self):
        return self.Development

class Notice(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Body = models.TextField()
    def __str__(self):
        return self.Title   
    def snippet(self):
        return self.Body[:50]+'...'

TYPE_CHOICES = (
    ("water","Water"),
    ("sanitation","Sanitation"),
)

SCALE_CHOICES = (
    ("large","Large Scale"),
    ("small","Small Scale"),
)

class Project(models.Model):
    Project_Type=models.CharField(max_length = 30,choices = TYPE_CHOICES, default = '--Project Type--')
    Project_Scale=models.CharField(max_length = 30,choices = SCALE_CHOICES, default = '--Project Scale--')
    def __str__(self):
        return self.Project_Type

class Request(models.Model):
    username=models.CharField(max_length=30) 
    Project_ID=models.IntegerField()
    RequestStatus=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class LargeScale(models.Model):
    Project_ID=models.IntegerField()
    Village_ID=models.IntegerField()
    Type=models.CharField(max_length=20)
    Organization_ID=models.IntegerField()
    Development=models.CharField(max_length=60)
    def __str__(self):
        return self.Development

class SmallScale(models.Model):
    Project_ID=models.IntegerField()
    Village_ID=models.IntegerField()
    Type=models.CharField(max_length=30)
    Personnel_ID=models.IntegerField()
    Facility=models.CharField(max_length=80)
    Location=models.CharField(max_length=40)
    def __str__(self):
        return self.Facility

class Village(models.Model):
    Village_ID=models.IntegerField()
    Village_name=models.CharField(max_length=80)
    State=models.CharField(max_length=80)
    def __str__(self):
        return self.Village_name

class Organization(models.Model):
    Organization_ID=models.IntegerField()
    Organization_name=models.CharField(max_length=100)
    def __str__(self):
        return self.Organization_name

class Appointment(models.Model):
    username=models.CharField(max_length=100)
    Personnel_ID=models.IntegerField()
    TimeSlot=models.DateTimeField()
    def __str__(self):
        return self.username

class OrganizationContact(models.Model):
    Organization_ID=models.IntegerField()
    Contact=models.IntegerField()
    
class LocalPersonnel(models.Model):
    Personnel_ID=models.IntegerField()
    Village_ID=models.IntegerField()
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=20)
    Occupation=models.CharField(max_length=40)
    def __str__(self):
        return self.First_name

class Community(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='community.jpg',blank=True)
    # add in author later
    def __str__(self):
        return self.title   
    def snippet(self):
        return self.body[:50]+'...'
