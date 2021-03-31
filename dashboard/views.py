from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import *
from django.contrib.auth.models import User
from .forms import ContactForm
from django.contrib import messages


@login_required(login_url="/login/")
def contact(request):
    ## TODO big Probelm with GET Method
    form = ContactForm()
    if request.GET.get('remove', False)  == 'true' :
        if request.GET.get('all', False) == 'true':
            Contacts.objects.all().delete()
        contact_id = request.GET.get('contact_id', False)
        Contacts.objects.filter(id=contact_id).delete()
    
    if request.method == "POST" :
        form = ContactForm(request.POST or None)
        if form.is_valid():
            nameandfamily= form.cleaned_data.get("nameandfamily")
            companyname= form.cleaned_data.get("companyname")
            mobile= form.cleaned_data.get("mobile")
            phone= form.cleaned_data.get("phone")
            address= form.cleaned_data.get("address")
            email= form.cleaned_data.get("email")
            user = request.user
            oj = Contacts(nameandfamily=nameandfamily,companyname=companyname,mobile=mobile,phone=phone,address=address,email=email,user=user)
            oj.save()
            messages.info(request, 'مخاطب با موفقیت ذخیره شد')

    profile  = UserProfile.objects.filter(user=request.user)
    context = {"contacts": Contacts.objects.filter(user=request.user),"user":request.user,"profiles":profile, 'form':form}
    return render(request, "dashboard/table-datatable.html", context)

@login_required(login_url="/login/")
def index(request):
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile}
    context['segment'] = 'index'

    html_template = loader.get_template( 'dashboard/main.html' )
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

        html_template = loader.get_template( 'dashboard/error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'dashboard/error-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def sakht(request):
    context = {"user":request.user}
    context['segment'] = 'index'
    html_template = loader.get_template( 'dashboard/page-maintenance.html' )
    return HttpResponse(html_template.render(context, request))