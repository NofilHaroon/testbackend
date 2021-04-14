from django.db import models

# Create your models here.

class Service(models.Model):
    ServiceID = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=100)

class Listing(models.Model):
    ListingId = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Rating = models.CharField(max_length=2)
    Description = models.CharField(max_length=500)
    Thumbnail = models.CharField(max_length=100)
    Img_one = models.CharField(max_length=100)
    Img_two = models.CharField(max_length=100)
    Img_three = models.CharField(max_length=100)

class Vendor(models.Model):
    VendorId = models.AutoField(primary_key=True)
    VendorName = models.CharField(max_length=100)
    Contact = models.CharField(max_length=20)
    Profilepic = models.CharField(max_length=100)
