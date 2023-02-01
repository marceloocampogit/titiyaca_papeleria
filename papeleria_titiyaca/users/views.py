from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView

from django.shortcuts import render, redirect

from .forms import UserUpdateForm, UserProfileForm

from .models import ProfileUser

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'users/login.html', context = context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {
                    'message': f'Bienvenido {username} !'
                }
                return render(request, 'home.html', context=context)
        
        else:
            form = AuthenticationForm()
            context = {
            'form': form,
            'errors': 'Usuario o contraseña incorrectos.'
        }
        return render(request, 'users/login.html', context=context)

def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context=context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #Guarda el usuario en la base de datos
            ProfileUser.objects.create(user = user)
            return redirect('home') #Redirecciona a la vista home

        context = {
            'errores': form.errors,
            'form': UserCreationForm()
        }    
        return render(request, 'users/register.html', context=context)

@login_required
def update_user(request):
    if request.method == 'GET':
        user = request.user
        form = UserUpdateForm(
            initial={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        )
        context = {
            'form': form
        }
        return render(request, 'users/update.html', context=context)
    elif request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'users/update.html', context=context)


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'

def update_profile_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={

            'phone': request.user.profile_user.phone,
            'birth_date': request.user.profile_user.birth_date,
            'city': request.user.profile_user.city,
            'country': request.user.profile_user.country,
            'profile_picture': request.user.profile_user.profile_picture

        })
        context = {
            'form': form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():

            user.profile_user.phone = form.cleaned_data.get('phone')
            user.profile_user.birth_date = form.cleaned_data.get('birth_date')
            user.profile_user.city = form.cleaned_data.get('city')
            user.profile_user.country = form.cleaned_data.get('country')
            user.profile_user.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile_user.save()

            return redirect('home') #Redirecciona a la vista home

        context = {
            'errores': form.errors,
            'form': UserProfileForm()
        }    
        return render(request, 'users/update_profile.html', context=context)

