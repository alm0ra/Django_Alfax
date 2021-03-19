from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from django.contrib.auth.models import User


def blog_view(request):
    context = {"articles": Article.objects.all(), "categories":Category.objects.all(),"last3":Article.objects.all()[:3]}
    return render(request, "blog/blog.html", context) #TODO Looking for a Blog Template