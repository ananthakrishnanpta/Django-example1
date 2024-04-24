from django.db import models

# Creating the model (schema for the database) for the Products table

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    pic = models.ImageField(upload_to = "products/", null= True) # adding image field
    