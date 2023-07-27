from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    spicy_level = models.IntegerField()
    category = models.ForeignKey
    cuisine = models.ForeignKey

    def __str__(self):
        return self.title
            
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name