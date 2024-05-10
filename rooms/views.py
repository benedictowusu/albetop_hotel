from django.shortcuts import render

# Create your views here.
def suite(request):
    return render(request, 'suite.html' )

def vip(request):
    return render(request, 'vip.html')

def standard(request):
    return render(request, 'standard.html')

def room(request):
    return render(request, 'room.html')