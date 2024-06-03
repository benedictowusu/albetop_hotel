from django.shortcuts import render, redirect
from .models import Suite, Standard, VIP, Book
from .forms import BookingForm

# Create your views here.
def suite(request):
    suiteroom = Suite.objects.all()
    return render(request, 'suite.html', {'suiterooms': suiteroom} )

def vip(request):
    viproom = VIP.objects.all().first()
    return render(request, 'vip.html', {'viprooms': viproom})

def standard(request):
    standroom = Standard.objects.all().first()
    return render(request, 'standard.html', {'standard': standroom})

def room(request):
    standardroom = Standard.objects.order_by('pricepernight').first()
    VIProom = VIP.objects.order_by('name').first()
    suiteroom = Suite.objects.order_by('numofSuites').first()
    return render(request, 'room.html', {'standardRooms': standardroom, 'VIProom' : VIProom, 'suiteroom' : suiteroom})

def book_room(request):
    global BookingForm
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            BookingForm = form.save()
            return redirect('Booking Confirmation', booking_code = Book.booking_code)
    else:
        form = BookingForm()
    return render(request,'book_room.html', {'booking_form': form})

def booking_confirmation(request, booking_code):
    booked = Book.objects.get(booking_code=booking_code)
    return render(request, 'booked.html', {'booked': booked})