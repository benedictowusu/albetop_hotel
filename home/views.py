from django.shortcuts import render
from rooms.models import Standard, VIP, Suite
# Create your views here.
def home(request):
    standardroom = Standard.objects.order_by('pricepernight').first()
    VIProom = VIP.objects.order_by('name').first()
    suiteroom = Suite.objects.order_by('numofSuites').first()
    return render(request, 'home.html', {'standardRooms': standardroom, 'VIProom' : VIProom, 'suiteroom' : suiteroom})


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')