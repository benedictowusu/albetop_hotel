from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.utils.dateformat import format
from django.db.models import Q
from .models import Booking, Rooms

# Create your views here.
@login_required
def bookroom(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            number_of_rooms = form.cleaned_data['number_of_rooms']

            # Find available room
            booked_rooms = Booking.objects.filter(
                Q(check_in__lte=check_out, check_out__gte=check_in)
            ).values_list('room_id', flat=True)

            available_room = Rooms.objects.exclude(id__in=booked_rooms).first()

            if available_room:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.room = available_room
                booking.save()
                return redirect(reverse('booking_success', args=[booking.booking_code]))
            else:
                form.add_error(None, "All rooms are booked")
    else:
        form = BookingForm()
        booked_dates = Booking.objects.values_list('check_in', 'check_out')

    return render(request, 'booking.html', {'bookingform': form, 'bookeddate': booked_dates} )

def booking_success(request, booking_code):
    return render(request, 'booking_success.html', {'booking_code': booking_code})