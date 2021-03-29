from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import income , expence , project
from django.contrib.auth.models import User
from .forms import incomeForm, expenceForm, projectForm
from dashboard.models import UserProfile


@login_required(login_url="/login/")
def index(request):
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile}
    return render(request, "dashboard/main_karonline.html",context) 

@login_required(login_url="/login/")
def make_project(request):
    form = projectForm()
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "form":form}
    return render(request, "dashboard/karon_project.html",context) 

@login_required(login_url="/login/")
def project_income(request):
    form = incomeForm()
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "form":form}
    return render(request, "dashboard/karon_income.html",context) 

@login_required(login_url="/login/")
def project_expence(request):
    form = expenceForm()
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "form":form}
    return render(request, "dashboard/karon_expence.html",context) 