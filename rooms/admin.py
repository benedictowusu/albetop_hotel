from django.contrib import admin
from .models import VIP, Standard,Suite, Book

# Register your models here.
admin.site.register(Suite)
admin.site.register(VIP)
admin.site.register(Standard)
admin.site.register(Book)