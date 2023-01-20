from django.shortcuts import render

from products.models import Categories, Products
from .forms import NewProductForm, NewCategoryForm

# Create your views here.

def create_product(request):
    if request.method == 'GET':
        context = {
            'form':NewProductForm()
        }
        return render(request,'products/create_product.html',context=context)
    elif request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                product_name = form.cleaned_data['product_name'],
                product_code = form.cleaned_data['product_code'],
                category_name = form.cleaned_data['category_name'],
                product_price = form.cleaned_data['product_price'],
                product_description = form.cleaned_data['product_description']           
            )
            context = { 
                'message': 'Producto creado exitosamente',
                'form':NewProductForm()}
            return render(request,'products/create_product.html',context=context)
        else:
            context = {
                'form_errors':form.errors,
                'form': NewProductForm()                 
            }
            return render(request,'products/create_product.html',context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        product = Products.objects.filter(product_name__contains=search)
    else:    
        product = Products.objects.all()    
    context = {
            'products':product,
    }
    return render(request, 'products/list_products.html', context=context)


def delete_product(request):
    return render(request, "home.html", context = {})

def update_product(request, pk):
    product = Products.objects.get(id = pk)

    if request.method == 'GET':
        context = {
            'form': NewProductForm(
                initial= {
                    'product_name': product.product_name,
                    'product_code': product.product_code,
                    'category_name': product.category_name,
                    'product_price': product.product_price,
                    'product_description': product.product_description,
                }
            )
        }

        return render(request,'products/update_product.html',context=context)
    elif request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            product.product_name = form.cleaned_data['product_name']
            product.product_code = form.cleaned_data['product_code']
            product.category_name = form.cleaned_data['category_name']
            product.product_price = form.cleaned_data['product_price']
            product.product_description = form.cleaned_data['product_description']
            product.save()           
            
            context = { 
                'message': 'Producto actualizado exitosamente',
                'form':NewProductForm()}
            return render(request,'products/update_product.html',context=context)
        else:
            context = {
                'form_errors':form.errors,
                'form': NewProductForm()                 
            }
            return render(request,'products/update_product.html',context=context)

def create_category(request):
    if request.method == 'GET':
        context = {
            'form':NewCategoryForm()
        }
        return render(request,'products/create_category.html',context=context)
    elif request.method == 'POST':
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            Categories.objects.create(
                category_name = form.cleaned_data['category_name']    
            )
            context = { 
                'message': 'Categoria creada exitosamente',
                'form':NewCategoryForm()
                }
            return render(request,'products/create_category.html',context=context)
        else:
            context = {
                'form_errors':form.errors,
                'form': NewCategoryForm()                 
            }
            return render(request,'products/create_category.html',context=context)

def list_categories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        category = Categories.objects.filter(category_name__contains=search)
    else:    
        category = Categories.objects.all()    
    context = {
            'categories':category,
    }
    return render(request, 'products/list_categories.html', context=context)

def delete_category(request):
    return render(request, "home.html", context = {})

def update_category(request):
    return render(request, "home.html", context = {})