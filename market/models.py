from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

