from django.db import models

# Create your models here.
class SerializerModel(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)

def __str__(self):
    return self.name
