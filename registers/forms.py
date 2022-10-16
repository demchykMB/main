import re
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):# Регистрация добавление емаил
    email = forms.EmailField()


    class META:
        model = User
        fields = ('username', 'email', "password1", "password2")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='имя', help_text="jjjj",
                               widget=forms.TextInput(attrs={'class': 'form control'}))
    password = forms.CharField(label='pass', help_text="jjjj",
                               widget=forms.PasswordInput(attrs={'class': 'form control'}))