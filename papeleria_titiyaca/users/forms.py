from django.contrib.auth.models import User
from django import forms

from .models import ProfileUser

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, label='Nombre de usuario')
    first_name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['phone', 'birth_date', 'city', 'country', 'profile_picture']