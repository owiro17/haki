from django.shortcuts import render
from rest_framework import viewsets
from .models import categoryData,ProductData
from .serializer import *
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = categoryData.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductData.objects.all()
    serializer_class = ProductSerializer