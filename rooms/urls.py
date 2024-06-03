from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path('', views.room, name='rooms'),
    path('standard/', views.standard, name='standard'),
    path('vip/', views.vip, name='vip'),
    path('suite/', views.Suite, name='suite'),
    path('book/', views.book_room, name='book_room'),
    path('confirmation/<uuid:booking_number>/', views.booking_confirmation, name='booking_confirmation'),
]