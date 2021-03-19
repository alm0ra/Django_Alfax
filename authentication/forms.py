# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import re
import urllib.parse


def conv(input_str):
    """
    This function convert Persian numbers to English numbers.
    
    Keyword arguments:
    input_str -- It should be string
    Returns: English numbers
    """
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)


def _multiple_replace(mapping, text):
    """
    Internal function for replace all mapping keys for a input string
    :param mapping: replacing mapping keys
    :param text: user input string
    :return: New string with converted mapping keys to values
    """
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "نام کاربری یا ایمیل",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "کلمه عبور",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(min_length=3,max_length=50,label="asdasd",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "نام  و نام خانوادگی",                
                "class": "form-control "
                
            }
        ))
    last_name = forms.CharField(min_length=3,max_length=50,label="",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "نام شرکت",                
                "class": "form-control"
            }
        ))
    username = forms.CharField(min_length=9,max_length=12,label="usererr",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "شماره موبایل",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(label="asdasd",
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "ایمیل",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(min_length=6,label="asdsad",
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "کلمه عبور",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(min_length=6,label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "تکرار کلمه عبور",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if (not '@' in email) and (not '.' in email):
            raise forms.ValidationError("ایمیل به درستی وارد نشده است")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("این ایمیل  قبلا ثبت شده است")
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2 :
            raise forms.ValidationError("رمز عبور و تکرار رمز عبور باید برابر باشد")
        return password1, password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username)<10 or len(username)>12:
            raise forms.ValidationError("شماره تلفن را به درستی وارد کنید")
        for item in username:
            if isinstance(item, int):
                raise forms.ValidationError("شماره تلفن باید فقط حاوی اعداد باشد")
                break
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("این شماره تلفن قبلا ثبت شده است")
        return conv(username)