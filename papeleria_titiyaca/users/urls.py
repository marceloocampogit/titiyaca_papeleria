from django.contrib import admin
from django.urls import path

from users.views import login_view, LogoutUser

urlpatterns = [
    path('login/', login_view),
    path('logout/', LogoutUser.as_view()),
    ]