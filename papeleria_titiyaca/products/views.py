from django.shortcuts import render

from products.models import Categories, Products
# Create your views here.


def home(request):
    return render(request, "home.html", context = {})

def create_product(request):
    return render(request, "home.html", context = {})

def view_products(request):
    return render(request, "products.html", context = {})

def search_product(request):
    return render(request, "home.html", context = {})