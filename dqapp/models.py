from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=80,blank=False)
    picture = models.TextField
    describe = models.TextField

class Wine(models.Model):
    name = models.CharField(max_length=80,blank=False)
    describe = models.TextField
    picture = models.TextField
    origin = models.CharField(max_length=120)
    brand = models.CharField(max_length=80)

