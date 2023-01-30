from django.contrib import admin
from django.urls import path

from users.views import login_view, LogoutUser, register_view, update_user

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', LogoutUser.as_view(), name= 'logout'),
    path('signup/', register_view, name='register_view'),
    path('update/', update_user, name='update_user'),
    ]