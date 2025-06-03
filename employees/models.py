from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

def __str__(self):
    return self.name

