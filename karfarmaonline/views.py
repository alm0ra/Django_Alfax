from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import income , expence , project
from django.contrib.auth.models import User
from .forms import incomeForm, expenceForm, projectForm
from dashboard.models import UserProfile

def index(request):

    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile}
    return render(request, "dashboard/main_karonline.html",context) 