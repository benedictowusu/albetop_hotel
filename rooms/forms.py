from django import forms
from django.forms import ModelForm
from .models import Book

class BookingForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['booking_code']