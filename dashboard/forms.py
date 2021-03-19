# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class contactform(forms.Form):
    namefamily = 1
    companyname = 1