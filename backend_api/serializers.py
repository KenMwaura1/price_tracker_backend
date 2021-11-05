from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'current_price', 'old_price', 'discount', 'image_url', 'link', 'category', 'date_added')
