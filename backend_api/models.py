from unicodedata import category

from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    current_price = models.CharField(max_length=50)
    old_price = models.CharField(max_length=50, null=True, blank=True)
    discount = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.CharField(max_length=2083, null=True, blank=True)
    link = models.CharField(max_length=2083)
    category = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

