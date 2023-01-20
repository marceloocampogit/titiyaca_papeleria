from django.contrib import admin

from products.models import Products, Categories

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'category_name', 'product_price', 'product_description')

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


