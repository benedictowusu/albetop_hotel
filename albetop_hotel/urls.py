from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('book/', include('book.urls')),
    path('rooms/', include('rooms.urls')),
    path('customer/', include('customer.urls')),
]
