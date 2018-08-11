from django.contrib import admin
from .models import Product, ShoppingList, Entry

# Register your models here.

admin.site.register(Product)
admin.site.register(ShoppingList)
admin.site.register(Entry)
