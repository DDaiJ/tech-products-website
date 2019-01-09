from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='imgs/')
    title = models.CharField(max_length=200)
    description = models.TextField()
