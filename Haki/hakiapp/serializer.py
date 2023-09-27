from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cartData
        fields = '__all__'
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categoryData
        fields ='__all__'