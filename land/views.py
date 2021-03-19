from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template




def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'landing/index.html' )
    return HttpResponse(html_template.render(context, request))