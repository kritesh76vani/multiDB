from django.db import models

# Create your models here.
class Product(models.Model):
    name      = models.CharField(max_length=500, null = True, blank = True)
    price     = models.FloatField(null = True, blank = True)
    unit      = models.IntegerField(null = True, blank = True)

def __str__(self):
    return self.name