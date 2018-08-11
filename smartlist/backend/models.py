from django.db import models

# Create your models here.

class ShoppingList(models.Model):
    name = models.CharField(max_length=200,
            help_text="Name of the shoppinglist")

class ProductList(models.Model):
    name = models.CharField(max_length=200,
            help_text="Name of the product")
    product_number = models.CharField(max_length=100,
            help_text="Short Name or product number")
    price = models.DecimalField(max_digits=15,
            decimal_places=2,
            help_text="Price of the product")
    category = models.CharField(max_length=100,
            help_text="Category of the product")

class Entrys(models.Model):
    shopping_list = models.ForeignKey(ShoppingList,
            models.CASCADE)
    product_list = models.ForeignKey(ProductList,
            models.CASCADE)
    name = models.CharField(max_length=200,
            help_text="Name of the list entry")
    product_number = models.CharField(max_length=100,
            help_text="Short Name or product number")
    price = models.DecimalField(max_digits=15,
            decimal_places=2,
            help_text="Price of the product")
    category = models.CharField(max_length=100,
            help_text="Category of the product")
    status = models.BooleanField(default=False,
            help_text="Status of the product")

