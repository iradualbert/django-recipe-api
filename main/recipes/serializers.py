import imp
from rest_framework import serializers
from .models import Category, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredient
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'