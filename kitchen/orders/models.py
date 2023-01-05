from django.db import models

# Create your models here.

class Order(models.Model):
    food        = models.CharField(max_length=100)
    quantity    = models.CharField(max_length=100)
    price       = models.CharField(max_length=100)
    status      = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.food