from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



class EditUser(UserChangeForm):
    username=forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=("username","first_name","last_name","email")