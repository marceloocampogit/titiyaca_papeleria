from users.models import ProfileUser
from django.contrib import admin  

@admin.register(ProfileUser)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone', 'birth_date', 'city', 'country', 'profile_picture')