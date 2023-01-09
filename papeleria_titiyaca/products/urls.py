from django.contrib import admin
from django.urls import path, include

from products.views import create_product, list_products, search_product, list_categories, create_category

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create-product/', create_product),
    path('create-category/', create_category),
    path('list-products/', list_products),
    path('search-product/', search_product),
    path('list-categories/', list_categories),

]
