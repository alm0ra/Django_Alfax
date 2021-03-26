from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from django.contrib.auth.models import User
from .forms import CommentForm

def blog_view(request):
    context = {
        "articles": Article.objects.published(),
        "categories":Category.objects.all(),
        "last3":Article.objects.filter(status= 'p').order_by('-publish')[:3]
     }

    return render(request, "blog/index-blog-2.html", context)

def article_detail(request,slug):
    form = CommentForm()
    article = Article.objects.filter(slug =slug)
    article_id = Article.objects.get(slug =slug).id
    article_comments = Article.objects.comments(article=article[0])
    article_comments_count = Article.objects.comment_count(article=article[0])
    post_cat  = Article.objects.categories(slug = slug)
    context = {
        "form":form,    
        "article": article,
        "Comments":article_comments,
        "Comments_count":article_comments_count, 
        "post_category":post_cat,
        "categories":Category.objects.all(),
        "last3":Article.objects.filter(status= 'p').order_by('-publish')[:3]
     }

    if request.method == "POST":
        form = CommentForm(request.POST or None)
        context = {
            "form":form,
            "article": article,
            "Comments":article_comments,
            "Comments_count":article_comments_count, 
            "post_category":post_cat,
            "categories":Category.objects.all(),
            "last3":Article.objects.filter(status= 'p').order_by('-publish')[:3]
        }
        
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            oj = Comments(name=name, email=email,text=text ,article =article[0])
            oj.save()

            context['form'] = CommentForm()
            return render(request, "blog/blog-post.html", context) 

    return render(request, "blog/blog-post.html", context) 