from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView

from django.shortcuts import render

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
                    'message': f'Bienivenido {username} !'
                }
                return render(request, 'home.html', context=context)
        
        else:
            form = AuthenticationForm()
            context = {
            'form': form,
            'errors': 'Usuario o contraseña incorrectos.'
        }
        return render(request, 'users/login.html', context=context)

class LogoutUser(LogoutView):
    template_name = 'users/logout.html'