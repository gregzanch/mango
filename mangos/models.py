from django.contrib.admin.utils import label_for_field
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.abbreviation}"

class Mango(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name