from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from orders.models import OrderStatus, PaymentMethod, Orders, OrderItems
from orders.forms import UpdateOrderItemsForm, DeleteOrderItemsForm, UpdateOrderStatusRegUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Orders ----------------------------------------------------------------
class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Orders
    template_name = 'orders/create_order.html'    
    fields = '__all__'
    # success_url = '/orders/list-orders/'   
    success_url = '/orders/create-order-items/'

class OrderUpdateView(LoginRequiredMixin, UpdateView):  
    model = Orders
    template_name = 'orders/update_order.html'        
    fields = '__all__'
    success_url = '/orders/list-orders/'      

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Orders
    template_name = 'orders/delete_order.html'        
    success_url = '/orders/list-orders/'    

def update_order_status_reg_user(request, pk): 
    order = Orders.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form':UpdateOrderStatusRegUserForm(
                initial={
                    'order_code':order.order_code,
                    'order_price':order.order_price ,
                    'creation_time':order.creation_time,                    
                    'payment_method_short':order.payment_method_short,
                    'client_name':order.client_name,
                    'status':order.status
                }
            )
        }
        return render(request,'orders/update_order_status_reg_user.html',context=context)

    elif request.method == 'POST':
        form = UpdateOrderStatusRegUserForm(request.POST)        
        if form.is_valid():            
            order.status = form.cleaned_data['status'] 
            order.save()
            order_code = order.order_code            
            context = { 
                'message':'Item de orden actualizado exitosamente',
                'order_code':order_code,                
            }                                                
            return redirect('list_orders')
        else:
            context = {
                'form_errors':form.errors,
                'form': UpdateOrderStatusRegUserForm()                 
            }
            return render(request,'orders/update_order_status_reg_user.html',context=context)   

# Esto iría con LoginRequiredMixin pero aun no tenemos manejo de usuarios y logins
# class PaymentMethodListView(LoginRequiredMixin, ListView):
class OrdersListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'orders/list_orders.html'    
    fields = '__all__'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        orderFilter = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('search')
        if query:
            return orderFilter.filter(order_code__contains=query)
        return orderFilter

# Order Items ----------------------------------------------------------------
class OrderItemsCreateView(LoginRequiredMixin, CreateView):
    model = OrderItems
    template_name = 'orders/create_order_items.html'    
    fields = '__all__'
    success_url = '/orders/create-order-items/'     

class OrderItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItems
    template_name = 'orders/update_order_items.html'    
    fields = '__all__'
    success_url = '/orders/list-order-items/pk/'

def update_order_item(request, pk): 
    order_item = OrderItems.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form':UpdateOrderItemsForm(
                initial={
                    'order_code':order_item.order_code,
                    'item_code':order_item.item_code,
                    'product_name':order_item.product_code.product_name,                    
                    'item_quantity':order_item.item_quantity
                    
                }
            )
        }
        return render(request,'orders/update_order_items.html',context=context)

    elif request.method == 'POST':
        form = UpdateOrderItemsForm(request.POST)        
        if form.is_valid():            
            order_item.item_quantity = form.cleaned_data['item_quantity'] 
            order_item.save()
            order_code = order_item.order_code            
            context = { 
                'message':'Item de orden actualizado exitosamente',
                'order_code':order_code,
                'order_items':OrderItems.objects.filter(order_code = order_code)
            }                                                
            return redirect('list_orders_items', pk=order_item.order_code.id)
        else:
            context = {
                'form_errors':form.errors,
                'form': UpdateOrderItemsForm()                 
            }
            return render(request,'orders/update_order_items.html',context=context)    

def delete_order_item(request, pk):
    order_item = OrderItems.objects.get(id=pk)
    if request.method == 'GET':        
        context = {
            'form':DeleteOrderItemsForm(
                initial={
                    'order_code':order_item.order_code,
                    'item_code':order_item.item_code,
                    'product_name':order_item.product_code.product_name,                    
                    'item_quantity':order_item.item_quantity
                    
                }
            )
        }
        return render(request,'orders/delete_order_item.html',context=context)
    elif request.method == 'POST':        
        order_code = order_item.order_code
        order_item.delete()
        context = { 
            'message':'Item de orden borrado exitosamente',
            'order_code':order_code,
            'order_items':OrderItems.objects.filter(order_code = order_code)  
            }
        return redirect('list_orders_items', pk=order_item.order_code.id)
        #return render(request,'orders/list_order_items.html',context=context)        

# def list_order_items(request, order_code):   
def list_order_items(request, pk):            
    order_items = OrderItems.objects.filter(order_code = pk)    
    paginator = Paginator(order_items, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
            # 'order_code':order_code,
            'order_items':page_obj,
    }
    return render(request,'orders/list_order_items.html',context=context)

# Order Status ----------------------------------------------------------
class OrderStatusCreateView(LoginRequiredMixin, CreateView):
    model = OrderStatus
    template_name = 'orders/create_order_status.html'    
    fields = '__all__'
    success_url = '/orders/list-orders-status/'    

class OrderStatusUpdateView(LoginRequiredMixin, UpdateView):  
    model = OrderStatus
    template_name = 'orders/update_order_status.html'        
    fields = '__all__'
    success_url = '/orders/list-orders-status/'  

class OrderStatusDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderStatus
    template_name = 'orders/delete_order_status.html'        
    success_url = '/orders/list-orders-status/'

# Esto iría con LoginRequiredMixin pero aun no tenemos manejo de usuarios y logins
# class PaymentMethodListView(LoginRequiredMixin, ListView):
class OrderStatusListView(ListView):
    model = OrderStatus
    template_name = 'orders/list_orders_status.html'
    paginate_by = 4

# Payment Method --------------------------------------------------------        
class PaymentMethodCreateView(LoginRequiredMixin, CreateView):
    model = PaymentMethod
    template_name = 'orders/create_payment_method.html'    
    fields = '__all__'
    success_url = '/orders/list-payment-methods/'        

class PaymentMethodUpdateView(LoginRequiredMixin, UpdateView):  
    model = PaymentMethod
    template_name = 'orders/update_payment_method.html'        
    fields = '__all__'
    success_url = '/orders/list-payment-methods/'    

class PaymentMethodDeleteView(LoginRequiredMixin, DeleteView):
    model = PaymentMethod
    template_name = 'orders/delete_payment_method.html'        
    success_url = '/orders/list-payment-methods/'

# Esto iría con LoginRequiredMixin pero aun no tenemos manejo de usuarios y logins
# class PaymentMethodListView(LoginRequiredMixin, ListView):
class PaymentMethodListView(LoginRequiredMixin, ListView):
    model = PaymentMethod
    template_name = 'orders/list_payment_methods.html'
    paginate_by = 4
    