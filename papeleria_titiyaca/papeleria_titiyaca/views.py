from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={})

def about_us(request):
    return render(request, 'aboutus.html', context={})