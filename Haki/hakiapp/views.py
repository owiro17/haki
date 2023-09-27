from django.shortcuts import render
from rest_framework import viewsets
from .models import categoryData,cartData,ProductData
from .serializer import *
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = categoryData.objects.all()
    serializer_class = CartSerializer