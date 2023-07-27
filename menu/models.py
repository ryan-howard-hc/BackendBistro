from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    spicy_level = models.IntegerField()

    def __str__(self):
        return self.title