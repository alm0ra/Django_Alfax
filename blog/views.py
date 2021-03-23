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
    article = Article.objects.filter(slug =slug)
    article_comments = Article.objects.comments(article=article[0])
    article_comments_count = Article.objects.comment_count(article=article[0])

    context = {
        "article": article,
        "Comments":article_comments,
        "Comments_count":article_comments_count, 
        "categories":Category.objects.all()
     }
    return render(request, "blog/blog-post.html", context) 