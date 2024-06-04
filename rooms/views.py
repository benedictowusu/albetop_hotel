from django.shortcuts import get_object_or_404, render, redirect
from .models import Suite, Standard, VIP, Book
from .forms import BookingForm

# Create your views here.
def suite(request):
    # view function to fetch details from the standard room mode
    suiteroom = Suite.objects.all()
    return render(request, 'suite.html', {'suiterooms': suiteroom} )

def vip(request):
    # view function to fetch details from the standard room mode
    viproom = VIP.objects.all().first()
    return render(request, 'vip.html', {'viprooms': viproom})

def standard(request):
    # view function to fetch details from the standard room mode
    standroom = Standard.objects.all().first()
    return render(request, 'standard.html', {'standard': standroom})

def room(request):
    # fetch details from the room models. It will only collect the first room instance
    standardroom = Standard.objects.order_by('pricepernight').first()
    VIProom = VIP.objects.order_by('name').first()
    suiteroom = Suite.objects.order_by('numofSuites').first()
    return render(request, 'room.html', {'standardRooms': standardroom, 'VIProom' : VIProom, 'suiteroom' : suiteroom})

def book_room(request):
    # continue if the method on the html is POST
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # save form if all fields are valid
            booking = form.save()
            return redirect('rooms:booking_confirmation', booking_code=booking.booking_code)
    else:
        # Else if method is GET
        form = BookingForm()
    return render(request,'book_room.html', {'booking_form': form})

def booking_confirmation(request, booking_code):
    # fetch booking model from database
    booked = get_object_or_404(Book, booking_code=booking_code)
    return render(request, 'booked.html', {'booked': booked})