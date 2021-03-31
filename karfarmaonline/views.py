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
from extensions.utils import place_value

@login_required(login_url="/login/")
def index(request):

    
    is_p_member = ProjectModel.objects.is_member_of(user =request.user) 
    is_manager = ProjectModel.objects.is_manager(user= request.user)

    if request.GET.get('remove', False)  == 'true' :
        project_id = request.GET.get('project_id', False)
        if ProjectModel.objects.is_manager_project(user=request.user, id =project_id):
            ProjectModel.objects.filter(id=project_id).delete()
            messages.info(request, "با موفقیت حذف شد * ")
    if request.GET.get('detail', False)  == 'true' :
        project_id = request.GET.get('project_id', False)
        if ProjectModel.objects.is_manager_project(user=request.user, id =project_id) or ProjectModel.objects.is_member_of_project(user=request.user, id =project_id):
            proj = ProjectModel.objects.get(id= project_id)
            profile  = UserProfile.objects.all().filter(user=request.user)
            total_expences = expence.objects.total(project=proj)
            total_incomes = income.objects.total(project=proj)
            total = expence.objects.total_project(project=proj)
            total_me_expence = expence.objects.total_project_user(user=request.user, project=proj)
            total_income_user = income.objects.total_per_user_project(user=request.user, project=proj)
            total_expences_user = expence.objects.total_per_user_project(user=request.user, project=proj)

            k1, k2, k3, k4, k5, k6 ,k7,k8 = expence.objects.Category_expence(project=proj)

            context = {
                "user":request.user,
                "profiles":profile,
                "detail":proj,
                "total_expences": place_value(total_expences) ,
                "total_incomes":  place_value(total_incomes),
                "total":  total,
                "total_me_expence": total_me_expence ,
                "total_income_user": place_value(total_income_user) ,
                "total_expences_user": place_value(total_expences_user) ,
                "k1": place_value(k1),
                "k2": place_value(k2),
                "k3": place_value(k3),
                "k4": place_value(k4),
                "k5": place_value(k5),
                "k6": place_value(k6) ,
                "k7": place_value(k7) ,
                "k8": place_value(k8)
                }

            return render(request, "dashboard/detail_project.html", context)


    if is_p_member or is_manager:
        my_expence = expence.objects.total_per_user(user= request.user)
        all_expence = expence.objects.filter(user=request.user) 
        my_income = income.objects.total_per_user(user=request.user)
        proj_count = ProjectModel.objects.project_count(user=request.user)
        expence_7day = expence.objects.total_last_7_days(user=request.user)
        profile  = UserProfile.objects.all().filter(user=request.user)
        proj_m= ProjectModel.objects.filter(Manager= request.user)
        proj= ProjectModel.objects.filter(Members= request.user)
        if my_expence is None :
            my_expence= 0 
        else : 
            my_expence = place_value( my_expence)

        if my_income is None :
            my_income = 0
        else : 
            my_income = place_value( my_income)

        if expence_7day is None :
            expence_7day = 0
        else : 
            expence_7day = place_value( expence_7day)

        context = {"user":request.user,
                        "profiles":profile,
                        "my_expence": my_expence,
                        "my_income":my_income ,
                        "proj_count":proj_count ,
                        "expence_7day": expence_7day,
                        "all_expence":all_expence, "p": True, 
                        "proj":proj, "proj_m":proj_m
                        }
        return render(request, "dashboard/main_karonline.html",context) 

    else:
        profile  = UserProfile.objects.all().filter(user=request.user)
        context = {"user":request.user,"profiles":profile, "enable":True, "p": True}
        return render(request, "dashboard/main_karonline.html",context)

@login_required(login_url="/login/")
def make_project(request):
    
    form = projectForm()
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "form":form, "p": True}

    
    
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
            return redirect('/dashboard/karfarmaonline/')
        else:
            form = projectForm(request.POST or None)
            context = {"user":request.user,"profiles":profile, "form":form, "p": True}
            render(request, "dashboard/karon_project.html",context) 

    return render(request, "dashboard/karon_project.html",context) 

@login_required(login_url="/login/")
def project_income(request):
    is_p_member = ProjectModel.objects.is_member_of(user =request.user) 
    is_manager = ProjectModel.objects.is_manager(user= request.user)
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile, "p": True}

    if is_p_member or is_manager:
        form = incomeForm()
        form.fields['project'].queryset = ProjectModel.objects.filter(Manager = request.user ) or ProjectModel.objects.filter(Members = request.user )
        profile  = UserProfile.objects.all().filter(user=request.user)
        context = {"user":request.user,"profiles":profile, "form":form, "p": True}

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
        context = {"user":request.user,"profiles":profile, "enable":True, "p": True}
        return render(request, "dashboard/main_karonline.html",context)

@login_required(login_url="/login/")
def project_expence(request):
    is_p_member = ProjectModel.objects.is_member_of(user =request.user) 
    is_manager = ProjectModel.objects.is_manager(user= request.user)
    profile  = UserProfile.objects.all().filter(user=request.user)
    context = {"user":request.user,"profiles":profile}
    
    if is_p_member or is_manager:
        form = expenceForm()
        form.fields['project'].queryset = ProjectModel.objects.filter(Manager = request.user ) or ProjectModel.objects.filter(Members = request.user )

        profile  = UserProfile.objects.all().filter(user=request.user)
        context = {"user":request.user,"profiles":profile, "form":form, "p": True}

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
        context = {"user":request.user,"profiles":profile, "enable":True, "p": True}
        return render(request, "dashboard/main_karonline.html",context)
