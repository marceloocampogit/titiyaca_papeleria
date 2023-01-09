from django import forms

class OrderStatusForm(forms.Form):
    status = forms.CharField(max_length=20)

class PaymentMethodForm(forms.Form):
    payment_method_large = forms.CharField(max_length=20)   
    payment_method_short = forms.CharField(max_length=3)   
    