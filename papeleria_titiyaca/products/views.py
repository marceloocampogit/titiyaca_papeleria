from django.shortcuts import render

from products.models import Categories, Products
from .forms import NewProductForm, NewCategoryForm
# Create your views here.

def create_product(request):
    if request.method == 'GET':
        context = {
            'form':NewProductForm()
        }
        return render(request,'orders/create_order_status.html',context=context)
    elif request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                status = form.cleaned_data['status'],
                product_name = form.cleaned_data['product_name'],
                product_code = form.cleaned_data['product_code'],
                category_name = form.cleaned_data['category_name'],
                product_price = form.cleaned_data['product_price'],
                product_description = form.cleaned_data['product_description']           
            )
            context = { 
                'message': 'Estado de orden creado exitosamente',
                'form':NewProductForm()
             }
            return render(request,'orders/create_order_status.html',context=context)
        else:
            context = {
                'form_errors':form.errors,
                'form': NewProductForm()                 
            }
            return render(request,'orders/create_order_status.html',context=context)
    return render(request, "home.html", context = {})

def list_products(request):

    products = Products.objects.all().values()
    context = {
        'Products': products
    }

    return render(request, "products.html", context = context)

def search_product(request):
    return render(request, "home.html", context = {})

def create_category(request):
    return render(request, "home.html", context = {})

def list_categories(request):

    categories = Categories.objects.all().values()
    context = {
        'Categories': categories
    }

    return render(request, "categories.html", context = context)