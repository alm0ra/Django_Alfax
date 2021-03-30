from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django import template
from .models import income , expence , ProjectModel
from django.contrib.auth.models import User
from .forms import incomeForm, expenceForm, projectForm
from dashboard.models import UserProfile


@login_required(login_url="/login/")
def index(request):
    is_p_member = ProjectModel.objects.is_member_of_project(user =request.user) 
    is_manager = ProjectModel.objects.is_manager(user= request.user)

    if is_p_member or is_manager:
        my_expence = expence.objects.total_per_user(user= request.user)
        all_expence = expence.objects.filter(user=request.user) 
        my_income = income.objects.total_per_user(user=request.user)
        proj_count = ProjectModel.objects.project_count(user=request.user)
        expence_7day = expence.objects.total_last_7_days(user=request.user)
        profile  = UserProfile.objects.all().filter(user=request.user)
        if my_expence['amount__sum'] is None :my_expence['amount__sum'] = 0
        if my_income['amount__sum'] is None :my_income['amount__sum'] = 0
        if expence_7day['amount__sum'] is None :expence_7day['amount__sum'] = 0

        context = {"user":request.user,
                        "profiles":profile,
                        "my_expence": my_expence['amount__sum'],
                        "my_income":my_income['amount__sum'] ,
                        "proj_count":proj_count ,
                        "expence_7day": expence_7day['amount__sum'],
                        "all_expence":all_expence, "p3": True
                        }
        return render(request, "dashboard/main_karonline.html",context) 

    else:
        profile  = UserProfile.objects.all().filter(user=request.user)
        context = {"user":request.user,"profiles":profile, "enable":True, "p3": True}
        return render(request, "dashboard/main_karonline.html",context)

@login_required(login_url="/login/")
def make_project(request):
    
    form = projectForm()
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "form":form, "p3": True}

    
    
    if request.method == "POST":

        form = projectForm(request.POST or None)

        if form.is_valid():
            Manager = request.user
            name = form.cleaned_data.get("name")
            zirbana = form.cleaned_data.get("zirbana")
            tedad_tabaqat = form.cleaned_data.get("tedad_tabaqat")
            address = form.cleaned_data.get("address")
            Members = form.cleaned_data.get("Members")
            description = form.cleaned_data.get("description")
            project_status = form.cleaned_data.get("project_status")
            Members= Members.replace(" ", "").split(",")
            if len(Members) > 1:
                instance = ProjectModel.objects.create(Manager=Manager,name=name,zirbana=zirbana,tedad_tabaqat= tedad_tabaqat,address= address,description= description,project_status=project_status)
                for item in Members:
                    is_user = ProjectModel.objects.is_user(str(item))
                    if not is_user:
                        messages.info(request, "کاربری با شماره همراه {} در سیستم یافت نشد ایشان باید در سیستم ثبت نام کنند".format(item))
                        return render(request, "dashboard/karon_project.html",context) 
                    user = User.objects.get(username=item)
                    instance.Members.add(user)


                instance.save()
            else:
                oj = ProjectModel(Manager=Manager,name=name,zirbana=zirbana,tedad_tabaqat= tedad_tabaqat,address= address,description= description,project_status=project_status)
                oj.save()
            messages.info(request, "با موفقیت ثبت شد")
        else:
            form = projectForm(request.POST or None)
            context = {"user":request.user,"profiles":profile, "form":form, "p3": True}
            render(request, "dashboard/karon_project.html",context) 

    return render(request, "dashboard/karon_project.html",context) 

@login_required(login_url="/login/")
def project_income(request):
    is_p_member = ProjectModel.objects.is_member_of_project(user =request.user) 
    is_manager = ProjectModel.objects.is_manager(user= request.user)
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "p3": True}

    if is_p_member or is_manager:
        form = incomeForm()
        form.fields['project'].queryset = ProjectModel.objects.filter(Manager = request.user ) or ProjectModel.objects.filter(Members = request.user )
        profile  = UserProfile.objects.all().filter(user=request.user)
        context = {"user":request.user,"profiles":profile, "form":form, "p3": True}

        if request.method == "POST":
            form = incomeForm(request.POST or None)

            if form.is_valid():
                user = request.user
                project = form.cleaned_data.get("project")
                title = form.cleaned_data.get("title")
                amount = form.cleaned_data.get("amount")
                description = form.cleaned_data.get("description")
                pay_mehod = form.cleaned_data.get("pay_mehod")
                category_pay = form.cleaned_data.get("category_pay")
                oj = income(user=user,project=project,title=title,amount=amount,description=description,pay_mehod=pay_mehod,category_pay=category_pay )
                oj.save()
                messages.info(request, "با موفقیت ثبت شد")

        return render(request, "dashboard/karon_income.html",context)
    else:
        context = {"user":request.user,"profiles":profile, "enable":True, "p3": True}
        return render(request, "dashboard/main_karonline.html",context)

@login_required(login_url="/login/")
def project_expence(request):
    is_p_member = ProjectModel.objects.is_member_of_project(user =request.user) 
    is_manager = ProjectModel.objects.is_manager(user= request.user)
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile}
    
    if is_p_member or is_manager:
        form = expenceForm()
        form.fields['project'].queryset = ProjectModel.objects.filter(Manager = request.user ) or ProjectModel.objects.filter(Members = request.user )

        profile  = UserProfile.objects.all().filter(user=request.user)
        context = {"user":request.user,"profiles":profile, "form":form, "p3": True}

        if request.method == "POST":
            form = expenceForm(request.POST or None)
            if form.is_valid():
                user = request.user
                project = form.cleaned_data.get("project")
                title = form.cleaned_data.get("title")
                amount = form.cleaned_data.get("amount")
                description = form.cleaned_data.get("description")
                pay_mehod = form.cleaned_data.get("pay_mehod")
                category_pay = form.cleaned_data.get("category_pay")
                oj = expence(user=user,project=project,title=title,amount=amount,description=description,pay_mehod=pay_mehod,category_pay=category_pay )

                oj.save()
                messages.info(request, "با موفقیت ثبت شد")

        return render(request, "dashboard/karon_expence.html",context) 
    else:
        context = {"user":request.user,"profiles":profile, "enable":True, "p3": True}
        return render(request, "dashboard/main_karonline.html",context)
