from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from orders.models import OrderStatus, PaymentMethod, Orders, OrderItems
from orders.forms import OrderStatusForm, PaymentMethodForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Orders ----------------------------------------------------------------
class OrderCreateView(CreateView):
    model = Orders
    template_name = 'orders/create_order.html'    
    fields = '__all__'
    # success_url = '/orders/list-orders/'   
    success_url = '/orders/create-order-items/'

class OrderUpdateView(UpdateView):  
    model = Orders
    template_name = 'orders/update_order.html'        
    fields = '__all__'
    success_url = '/orders/list-orders/'      

class OrderDeleteView(DeleteView):
    model = Orders
    template_name = 'orders/delete_order.html'        
    success_url = '/orders/list-orders/'    

# Esto iría con LoginRequiredMixin pero aun no tenemos manejo de usuarios y logins
# class PaymentMethodListView(LoginRequiredMixin, ListView):
class OrdersListView(ListView):
    model = Orders
    template_name = 'orders/list_orders.html'    

# Order Items ----------------------------------------------------------------
class OrderItemsCreateView(CreateView):
    model = OrderItems
    template_name = 'orders/create_order_items.html'    
    fields = '__all__'
    success_url = '/orders/create-order-items/'     

class OrderItemsUpdateView(UpdateView):
    model = OrderItems
    template_name = 'orders/update_order_items.html'    
    fields = '__all__'
#    fields
    success_url = '/orders/list-order-items/pk/'

################
def delete_order_item(request, pk):
    order_item = OrderItems.objects.get(id=pk)
    if request.method == 'GET':        
        context = {
            'order_item':order_item,
        }
        return render(request,'orders/delete_order_item.html',context=context)
    elif request.method == 'POST':        
        order_code = order_item.order_code
        order_item.delete()
        context = { 
            'message':'Item de orden borrado exitosamente',
            'order_code':order_code  
            }
        return render(request,'orders/delete_order_item.html',context=context)   
        #return redirect('list_order_items')            
################

################
def list_order_items(request, order_code):    
    order_items = OrderItems.objects.filter(order_code = order_code)    
    context = {
            'order_code':order_code,
            'order_items':order_items,
    }
    return render(request,'orders/list_order_items.html',context=context)
################

# Order Status ----------------------------------------------------------
class OrderStatusCreateView(CreateView):
    model = OrderStatus
    template_name = 'orders/create_order_status.html'    
    fields = '__all__'
    success_url = '/orders/list-orders-status/'    

class OrderStatusUpdateView(UpdateView):  
    model = OrderStatus
    template_name = 'orders/update_order_status.html'        
    fields = '__all__'
    success_url = '/orders/list-orders-status/'  

class OrderStatusDeleteView(DeleteView):
    model = OrderStatus
    template_name = 'orders/delete_order_status.html'        
    success_url = '/orders/list-orders-status/'

# Esto iría con LoginRequiredMixin pero aun no tenemos manejo de usuarios y logins
# class PaymentMethodListView(LoginRequiredMixin, ListView):
class OrderStatusListView(ListView):
    model = OrderStatus
    template_name = 'orders/list_orders_status.html'

# Payment Method --------------------------------------------------------
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
        
class PaymentMethodCreateView(CreateView):
    model = PaymentMethod
    template_name = 'orders/create_payment_method.html'    
    fields = '__all__'
    success_url = '/orders/list-payment-methods/'        

class PaymentMethodUpdateView(UpdateView):  
    model = PaymentMethod
    template_name = 'orders/update_payment_method.html'        
    fields = '__all__'
    success_url = '/orders/list-payment-methods/'    

class PaymentMethodDeleteView(DeleteView):
    model = PaymentMethod
    template_name = 'orders/delete_payment_method.html'        
    success_url = '/orders/list-payment-methods/'

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

# Esto iría con LoginRequiredMixin pero aun no tenemos manejo de usuarios y logins
# class PaymentMethodListView(LoginRequiredMixin, ListView):
class PaymentMethodListView(ListView):
    model = PaymentMethod
    template_name = 'orders/list_payment_methods.html'
    