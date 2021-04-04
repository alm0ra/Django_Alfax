# -*- encoding: utf-8 -*-


from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm



def forget_view(request):
    return render(request, "accounts/auth-forgot-password.html")

def verify_view(request):
    return render(request, "accounts/auth-verification-number.html")

def logout_view(request):
    logout(request)
    return redirect("/login")
    
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("/dashboard/karfarmaonline/")
            
            else:    
                messages.info(request, "نام کاربری یا کلمه عبور اشتباه می باشد")   
        else:
            messages.info(request, "خطا در اعتبار سنجی فرم")   

    return render(request, "accounts/auth-login.html", {"form": form})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            success = True
            
            return redirect("/dashboard/karfarmaonline/")
        else:
            return render(request, "accounts/auth-register.html", context)

    else:
        form = SignUpForm()

    return render(request, "accounts/auth-register.html", {"form": form, "msg" : messages, "success" : success })
