from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path('suite/', views.suite, name='suite'),
    path('vip/', views.vip, name='vip'),
    path('standard', views.standard, name='standard')
]