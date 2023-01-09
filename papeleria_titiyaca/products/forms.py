from django import forms

class NewProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_code = forms.IntegerField()
    category_name = forms.CharField(max_length=100)
    product_price = forms.FloatField()
    product_description = forms.CharField(max_length=200)

class NewCategoryForm(forms.Form):
    category_name = forms.CharField(max_length=100)