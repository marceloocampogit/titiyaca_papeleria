from django.contrib.auth.models import User
from django import forms

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name']