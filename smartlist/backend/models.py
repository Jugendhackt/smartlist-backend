from django.db import models

# Create your models here.

class ShoppingList(models.Model):
    name = models.CharField(max_length=200,
            help_text="Name of the shoppinglist")

    def __str__():
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,
            help_text="Name of the product")
    product_number = models.CharField(max_length=100,
            help_text="Short Name or product number")
    price = models.DecimalField(max_digits=15,
            decimal_places=2,
            help_text="Price of the product")
    category = models.CharField(max_length=100,
            help_text="Category of the product")

    def __str__():
        return self.name

class Entry(models.Model):
    shopping_list = models.ForeignKey(ShoppingList,
            models.CASCADE)
    product = models.ForeignKey(Product,
            models.CASCADE)
    name = models.CharField(max_length=200,
            help_text="Name of the list entry")
    price = models.DecimalField(max_digits=15,
            decimal_places=2,
            help_text="Price of the product")
    category = models.CharField(max_length=100,
            help_text="Category of the product")
    STATUS = (
            ("open", "Currently not buyed"),
            ("closed", "Already bought"),
    )
    status = models.CharField(max_length=1,
            choices=STATUS,
            help_text="Status of the product")

    def __str__():
        return self.name

    class Meta:
        verbose_name_plural = ("Entries")
