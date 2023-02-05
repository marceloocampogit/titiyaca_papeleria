from django.urls import path

from users.views import login_view, LogoutUser, register_view, update_user, update_profile_user

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', LogoutUser.as_view(), name= 'logout'),
    path('signup/', register_view, name='register_view'),
    path('update/', update_user, name='update_user'),
    path('update/profile/', update_profile_user, name='update_profile_user'),
    ]