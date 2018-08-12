from rest_framework import serializers
from .models import Product, ShoppingList, Entry

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'product_number', 'price', 'category')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('shopping_list', 'product', 'name', 'price', 'category', 'status')
