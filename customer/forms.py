from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    phoneNumber = forms.IntegerField()
    firstName = forms.CharField(max_length=250)
    lastName = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email','phoneNumber', 'password1', 'password2')

    def emailCheck(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email exist')
        return email