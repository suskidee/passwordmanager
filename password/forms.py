from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import New


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AddForm(forms.ModelForm):
    class Meta:
        model = New
        fields = [
            'website',
            'username',
            'password'
        ]


class SearchForm(forms.Form):
    username = forms.CharField()
