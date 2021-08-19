from django import forms
from .models import User
from django.core import validators

class studentregistration(forms.ModelForm):
    class Meta:
        model =  User
        fields  = ['name','email' , 'password' , 'phon']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phon':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }