from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Categories, Products
from .forms import NewProductForm, NewCategoryForm

# Create your views here.

# ------------------------------------------- Products GViews ------------------------------------------- #
class CreateProduct(LoginRequiredMixin, CreateView):
    model = Products
    template_name = 'products/create_product.html'
    fields = '__all__'
    success_url = '/products/list-products/'

class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = 'products/delete_product.html'
    success_url = '/products/list-products/'

class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = 'products/update_product.html'
    fields = '__all__'
    success_url = '/products/list-products/'

class ListProducts(LoginRequiredMixin, ListView):
    model = Products
    template_name = 'products/list_products.html'
    fields = '__all__'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        productFilter = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('search')
        if query:
            return productFilter.filter(product_name__contains=query)
        return productFilter

# ------------------------------------------- Categories GViews ------------------------------------------- #

class CreateCategory(LoginRequiredMixin, CreateView):
    model = Categories
    template_name = 'products/create_category.html'
    fields = '__all__'
    success_url = '/products/list-categories/'

class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Categories
    template_name = 'products/delete_category.html'
    success_url = '/products/list-categories/'

class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Categories
    template_name = 'products/update_category.html'
    fields = '__all__'
    success_url = '/products/list-categories/'

class ListCategories(LoginRequiredMixin, ListView):
    model = Categories
    template_name = 'products/list_categories.html'
    fields = '__all__'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        categoryFilter = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('search')
        if query:
            return categoryFilter.filter(category_name__contains=query)
        return categoryFilter

# ----------------------------------------------------------------------------------------------------------- #