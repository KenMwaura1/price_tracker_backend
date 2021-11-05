from unicodedata import category

from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


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

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

"""
class Product(models.Model):
	title=models.CharField(max_length=500)
	current_price=models.FloatField(max_length=30)
	product_url=models.URLField(max_length=1000)
	img_src=models.URLField(max_length=1000)
	desire_price=models.FloatField(max_length=30)
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('user-products',args=[self.author.username])
"""
