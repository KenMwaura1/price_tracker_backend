from django.contrib import admin

from .models import Product
from .models import Profile


admin.site.register(Product)
admin.site.register(Profile)

