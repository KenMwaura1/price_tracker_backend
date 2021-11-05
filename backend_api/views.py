from django.shortcuts import render
from rest_framework import viewsets

from .models import Product

# Create your views here.
from .serializers import ProductSerializer


def index(request):
    return render(request, 'index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-date_added')
    serializer_class = ProductSerializer
