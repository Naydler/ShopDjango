from django.db import models

# Create your models here.

class product (models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    size = models.CharField(max_length=1)
