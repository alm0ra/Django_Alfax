from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from django.contrib.auth.models import User




@login_required(login_url="/login/")
def contact(request):
    ## TODO big Probelm with GET Method
    if request.GET.get('remove', False)  == 'true' :
        if request.GET.get('all', False) == 'true':
            Contacts.objects.all().delete()
        contact_id = request.GET.get('contact_id', False)
        Contacts.objects.filter(id=contact_id).delete()

    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"contacts": Contacts.objects.all(),"user":request.user,"profiles":profile}
    return render(request, "table-datatable.html", context)

@login_required(login_url="/login/")
def index(request):
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile}
    context['segment'] = 'index'

    html_template = loader.get_template( 'main.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def contacts(request):
    pass