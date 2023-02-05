from django.urls import path

from products.views import CreateProduct, UpdateProduct, DeleteProduct, ListProducts, CreateCategory, ListCategories, UpdateCategory, DeleteCategory

urlpatterns = [
    # Products
    path('create-product/', CreateProduct.as_view(), name='create_product'),
    path('list-products/', ListProducts.as_view(), name='list_products'),
    path('update-product/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
    path('delete-product/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),

    #Categories
    path('create-category/', CreateCategory.as_view(), name='create_category'),
    path('list-categories/', ListCategories.as_view(), name='list_categories'),
    path('update-category/<int:pk>/', UpdateCategory.as_view(), name='update_category'),
    path('delete-category/<int:pk>/', DeleteCategory.as_view(), name='delete_category'),

]
