from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from members.forms import EditUser
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class RegisterView(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class MyPasswordsChangeView(SuccessMessageMixin,PasswordChangeView):
    success_message="your password has been changed successfully!!"
    form_class=PasswordChangeForm
    template_name='registration/password.html'
    success_url=reverse_lazy('home')

class MyPasswordsChangeDoView(SuccessMessageMixin,PasswordChangeDoneView):
    success_message="your password has been changed successfully!!"
    template_name='registration/done.html'


class EditView(SuccessMessageMixin,generic.UpdateView):
    form_class=EditUser
    context_object_name='me'
    success_message="your profile has been updated successfully!!"
    template_name='registration/edit.html'
    success_url=reverse_lazy('myaccount')
    
    def get_object(self):
        return self.request.user

