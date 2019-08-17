from django.db import models

# Create your models here.
class Menu(models.Model):
    food = models.CharField(max_length=30)
    description = models.TextField()

class Customer(models.Model):
    status = models.CharField(max_length=30)
    cart = models.TextField()

class Deliver(models.Model):
    order = models.TextField()
    status = models.CharField(max_length=30)
