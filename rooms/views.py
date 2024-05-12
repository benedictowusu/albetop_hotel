from django.shortcuts import render
from .models import Suite, Standard, VIP

# Create your views here.
def suite(request):
    suiteroom = Suite.objects.all()
    return render(request, 'suite.html', {'suiterooms': suiteroom} )

def vip(request):
    viproom = VIP.objects.all()
    return render(request, 'vip.html', {'viprooms': viproom})

def standard(request):
    standardroom = Standard.objects.all()
    return render(request, 'standard.html', {'standardrooms': standardroom})

def room(request):
    standard = Standard.objects.all()
    viproom = VIP.objects.all()
    suiteroom = Suite.objects.all()
    return render(request, 'room.html', {'standard': standard})