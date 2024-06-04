from django import forms
from django.forms import ModelForm
from .models import Book

class BookingForm(ModelForm):
    class Meta:
        model = Book
        # Display all model instances in BOOK except the booking_code
        exclude = ['booking_code']