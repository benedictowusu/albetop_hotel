from django.urls import path
from .views import bookroom, booking_success

app_name = 'booking'
urlpatterns = [
    path('bookroom/', bookroom, name='bookroom'),
    path('booking_success/<str:booking_code>/', booking_success, name='booking_success'),
]