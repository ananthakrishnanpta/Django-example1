from django.db import models

# Create your models here.

class User(models.Model): # This creates a 'User' table in the database # create table User()
    user_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length = 255) # name, VARCHAR(255)
    age = models.BigIntegerField(null=True)


# Creating the model (schema for the database) for the Products table

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
