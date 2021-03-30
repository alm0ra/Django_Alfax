from .models import income , expence, ProjectModel
from django.forms import TextInput, EmailInput,Textarea, Select,NumberInput
from django import forms

class incomeForm(forms.ModelForm):
    class Meta:
        model = income
        fields = ('project','title','amount','description','pay_mehod','category_pay')
        widgets = {
            'project': Select(attrs={'class':'form-control', 'placeholder':'پروژه را انتخاب کنید'}),
            'title': TextInput(attrs={'class':'form-control', 'placeholder':'عنوان درآمد را وارد کنید'}),
            'amount': TextInput(attrs={'class':'form-control', 'placeholder':'مقدار درآمد به تومان را وارد کنید'}),
            'description' : Textarea(attrs={'class':'form-control', 'placeholder':'توضیحات'}),
            'pay_mehod':Select(attrs={'class':'form-control', 'placeholder':'روش پرداخت'}),
            'category_pay':Select(attrs={'class':'form-control', 'placeholder':'دسنه بندی'}),
        }

class expenceForm(forms.ModelForm):
    class Meta:
        model = expence
        fields = ('project','title','amount','description','pay_mehod','category_pay')
        widgets = {
            'project': Select(attrs={'class':'form-control', 'placeholder':'پروژه را انتخاب کنید'}),
            'title': TextInput(attrs={'class':'form-control', 'placeholder':'عنوان هزینه کرد را وارد کنید'}),
            'amount': TextInput(attrs={'class':'form-control', 'placeholder':'مقدار هزینه کرد به تومان را وارد کنید'}),
            'description' : Textarea(attrs={'class':'form-control', 'placeholder':'توضیحات '}),
            'pay_mehod':Select(attrs={'class':'form-control', 'placeholder':'روش پرداخت'}),
            'category_pay':Select(attrs={'class':'form-control', 'placeholder':'دسته بندی'}),
        }

class projectForm(forms.ModelForm):
    Members = forms.CharField(min_length=3,max_length=200,label="asdasd",required = False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "برای اضافه کردن شرا به پروژه شماره تلفن آنهارا وارد و با ','از هم جدا کنید",                
                "class": "form-control "
                
            }
        ))
    class Meta:
        model = ProjectModel
        fields = ('name','zirbana','tedad_tabaqat','address','Members','description','project_status')
        widgets = {
            'name':TextInput(attrs={'class':'form-control','placeholder':'نام پروژه را وارد کنید'}),
            'zirbana':NumberInput(attrs={'class':'form-control','placeholder':'مساحت زیر بنای پروژه را وارد کنید'}),
            'tedad_tabaqat':NumberInput(attrs={'class':'form-control','placeholder':'تعداد طبقات پروژه را وارد کنید'}),
            'address':TextInput(attrs={'class':'form-control','placeholder':'آدرس پروژه را وارد کنید'}),
            'description':Textarea(attrs={'class':'form-control','placeholder':'توضیحات پروژه را وارد کنید'}),
            'project_status':Select(attrs={'class':'form-control','placeholder':'انتخاب کنید'}),
        }