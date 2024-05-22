from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'number_of_rooms']
        widgets = {
            "check In": forms.DateInput(attrs={'type': 'date'}),
            "check Out": forms.DateInput(attrs={'type': 'date'})
        }