# -*- encoding: utf-8 -*-

from .models import Contacts
from django import forms
from django.forms import TextInput, EmailInput,Textarea, Select,NumberInput
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ('nameandfamily','companyname','mobile','phone','address','email')
        widgets = {
            'nameandfamily':TextInput(attrs={'class':'form-control','placeholder':'نام و نام خانوادگی'}),
            'companyname':TextInput(attrs={'class':'form-control','placeholder':'نام شرکت'}),
            'mobile':NumberInput(attrs={'class':'form-control','placeholder':'شماره همراه'}),
            'phone':NumberInput(attrs={'class':'form-control','placeholder':'تلفن ثابت'}),
            'address':TextInput(attrs={'class':'form-control','placeholder':'آدرس'}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':'ایمیل'}),
        }
    

