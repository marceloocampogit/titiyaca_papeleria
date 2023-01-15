from django.contrib import admin
from django.urls import path

from products.views import create_product, list_products, list_categories, create_category, update_product

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create-product/', create_product, name='create_product'),
    path('list-products/', list_products, name='list_products'),
    path('update-product/<int:pk>', update_product, name='update_product'),

    path('create-category/', create_category, name='create_category'),
    path('list-categories/', list_categories, name='list_categories'),

]
