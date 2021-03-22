from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from django.contrib.auth.models import User


def blog_view(request):
    context = {"articles": Article.objects.filter(status= 'p').order_by('-publish'), "categories":Category.objects.all(),"last3":Article.objects.filter(status= 'p').order_by('-publish')[:3]}
    return render(request, "blog/index-blog-2.html", context)

def article_detail(request,slug):
    context = {
        "articles": Article.objects.filter(slug= slug).order_by('-publish'),
        "categories":Category.objects.all(),
        "last3":Article.objects.filter(status= 'p').order_by('-publish')[:3],
        "comments":Comments.objects.filter(article=Article.objects.filter(slug=slug)).order_by('-date') 
     }
    return render(request, "blog/blog-post.html", context) 