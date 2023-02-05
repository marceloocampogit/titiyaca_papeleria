from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home, about_us
from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', about_us, name='about_us'),
    path('', home, name='home'),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
