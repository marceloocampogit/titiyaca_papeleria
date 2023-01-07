from django.contrib import admin
from django.urls import path, include

from products.views import home, create_product, view_products, search_product

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    path('crear-producto', create_product),
    path('mostrar-productos', view_products),
    path('buscar-producto', search_product),
    path('', home),


]
