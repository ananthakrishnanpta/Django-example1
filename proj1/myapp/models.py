from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Creating the model (schema for the database) for the Products table

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    pic = models.ImageField(upload_to = "products/", null= True) # adding image field

