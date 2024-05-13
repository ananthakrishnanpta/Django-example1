from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Creating the model (schema for the database) for the Products table

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    pic = models.ImageField(upload_to = "products/", null= True) # adding image field



# class Reviews(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     stars = models.IntegerChoices([1,2,3,4,5])
#     body = models.TextField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)