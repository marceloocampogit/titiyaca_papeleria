from django import forms
from orders.models import OrderStatus

class UpdateOrderStatusRegUserForm(forms.Form):
    order_code = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    order_price = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    creation_time = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly':'readonly'}))    
    payment_method_short = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))         
    client_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    status = forms.ModelChoiceField(queryset=OrderStatus.objects.all())

class UpdateOrderItemsForm(forms.Form):
    order_code = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    item_code = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))    
    product_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    item_quantity = forms.IntegerField()

class DeleteOrderItemsForm(forms.Form):
    order_code = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    item_code = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))    
    product_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    item_quantity = forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    