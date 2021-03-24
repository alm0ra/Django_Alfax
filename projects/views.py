from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from blog.models import *
from django.contrib.auth.models import User


def project_detail(request,slug):
    project = Projects_detail.objects.filter(project_slug =slug)
    last4project = Projects_detail.objects.filter(status='p')

    post_cat  = Projects_detail.objects.categories(slug = slug)

    context = {
        "project": project,
        "last4":last4project, 
        "project_category":post_cat,
        "categories":Category.objects.all(),
        "last3":Article.objects.filter(status= 'p').order_by('-publish')[:3]
     }
    return render(request, "projects/project_detail.html", context) 