from .models import income , expence, project
from django.forms import TextInput, EmailInput,Textarea, Select,NumberInput
from django import forms

class incomeForm(forms.ModelForm):
    class Meta:
        model = income
        fields = ('project','title','amount','description','pay_mehod','category_pay')
        widgets = {
            'project': Select(attrs={'class':'form-control'}),
            'title': TextInput(attrs={'class':'form-control'}),
            'amount': TextInput(attrs={'class':'form-control'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'pay_mehod':Select(attrs={'class':'form-control'}),
            'category_pay':Select(attrs={'class':'form-control'}),
        }

class expenceForm(forms.ModelForm):
    class Meta:
        model = expence
        fields = ('project','title','amount','description','pay_mehod','category_pay')
        widgets = {
            'project': Select(attrs={'class':'form-control'}),
            'title': TextInput(attrs={'class':'form-control'}),
            'amount': TextInput(attrs={'class':'form-control'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'pay_mehod':Select(attrs={'class':'form-control'}),
            'category_pay':Select(attrs={'class':'form-control'}),
        }

class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ('name','zirbana','tedad_tabaqat','address','Members','description','project_status')
        widgets = {
            'name':TextInput(attrs={'class':'form-control'}),
            'zirbana':NumberInput(attrs={'class':'form-control'}),
            'tedad_tabaqat':NumberInput(attrs={'class':'form-control'}),
            'address':TextInput(attrs={'class':'form-control'}),
            'Members':TextInput(attrs={'class':'form-control'}),
            'description':Textarea(attrs={'class':'form-control'}),
            'project_status':Select(attrs={'class':'form-control'}),
        }