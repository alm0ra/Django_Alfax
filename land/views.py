from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import LandingPage 
from blog.models import Article

def index(request):
    
    context = {'landing':LandingPage.objects.all()[:1],
            'articles':Article.objects.filter(status='p').order_by('-publish')[:3]}
    context['segment'] = 'index'

    html_template = loader.get_template( 'landing/index.html' )
    return HttpResponse(html_template.render(context, request))

def resume(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'landing/resume.html' )
    return HttpResponse(html_template.render(context, request))