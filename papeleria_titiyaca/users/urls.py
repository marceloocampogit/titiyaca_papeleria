from django.contrib import admin
from django.urls import path

from users.views import login_view, LogoutUser, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutUser.as_view(), name= 'logout'),
    path('signup/', register_view, name='signup'),
    ]