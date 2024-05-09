from django.contrib import admin
from .models import Suite, VIP, Standard

# Register your models here.
admin.site.register(Suite)
admin.site.register(VIP)
admin.site.register(Standard)