from django.shortcuts import render

from orders.models import OrderStatus, PaymentMethod
from .forms import OrderStatusForm, PaymentMethodForm

# Create your views here.
def create_order_status(request):
    if request.method == 'GET':
        context = {
            'form':OrderStatusForm()
        }
        return render(request,'orders/create_order_status.html',context=context)
    elif request.method == 'POST':
        form = OrderStatusForm(request.POST)
        print(form)
        if form.is_valid():
            OrderStatus.objects.create(
                status = form.cleaned_data['status'],                
            )
            context = { 
                'message': 'Estado de orden creado exitosamente',
                'form':OrderStatusForm()
             }
            return render(request,'orders/create_order_status.html',context=context)
        else:
            context = {
                'form_errors':form.errors,
                'form': OrderStatusForm()                 
            }
            return render(request,'orders/create_order_status.html',context=context)

def list_orders_status(request):
    if 'search' in request.GET:
        search = request.GET['search']
        orders_status = OrderStatus.objects.filter(name__contains=search)
    else:    
        orders_status = OrderStatus.objects.all()    
    context = {
            'orders_status':orders_status,
    }
    return render(request, 'orders/list_orders_status.html', context=context)

def create_payment_method(request):
    if request.method == 'GET':
        context = {
            'form':PaymentMethodForm()
        }
        return render(request,'orders/create_payment_method.html',context=context)
    elif request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        print(form)
        if form.is_valid():
            PaymentMethod.objects.create(
                payment_method_large = form.cleaned_data['payment_method_large'], 
                payment_method_short = form.cleaned_data['payment_method_short'],
            )
            context = { 
                'message': 'Método de pago creado exitosamente',
                'form':PaymentMethodForm()
             }
            return render(request,'orders/create_payment_method.html',context=context)
        else:
            context = {
                'form_errors':form.errors,
                'form': PaymentMethodForm()                 
            }
            return render(request,'orders/create_payment_method.html',context=context)

def list_payment_methods(request):
    if 'search' in request.GET:
        search = request.GET['search']
        payment_methods = PaymentMethod.objects.filter(name__contains=search)
    else:    
        payment_methods = PaymentMethod.objects.all()    
    context = {
            'payment_methods':payment_methods,
    }
    return render(request, 'orders/list_payment_methods.html', context=context)
