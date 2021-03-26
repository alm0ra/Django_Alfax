from django import forms
from .models import Comments
from django.forms import TextInput, EmailInput,Textarea

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text')
        widgets = {'name': TextInput(attrs={'class':"form-control"}),
                    'email': EmailInput(attrs={'class':"form-control" }),
                    'text': Textarea(attrs={'class':"form-control",'rows':"8",'maxlength':"5000"  }),}

                    

            