from ast import Mod
import imp
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class CustomAccountForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'password1', 'password2']
