from django.shortcuts import render
from django.views import generic
from myaccount.models import Products,Profile
from django.urls import reverse_lazy
from myaccount.forms import AddProductForm,CreateProfileForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin




class AddProduct(SuccessMessageMixin,generic.CreateView):
    model=Products
    template_name='myaccount/add_new.html'
    form_class=AddProductForm
    success_message="your item has been added successfully!!"
    sucess_url=reverse_lazy('myaccount')
   
 

class CreateProfile(generic.CreateView):
    model=Profile
    template_name='myaccount/create_profile.html'
    form_class=CreateProfileForm
    sucess_url=reverse_lazy('myaccount/home.html')
   



class MyProductView(generic.ListView):
    model=Products
    template_name='myaccount/home.html'
    
    ordering='-id'

    def get_context_data(self, *args, **kwargs):
        context=super(MyProductView,self).get_context_data(*args, **kwargs)
        product=Products.objects.all()
        info=Profile.objects.all()
        context['product']=product
        context['info']=info
        return context

        def get_object(self):
            return self.request.user
        

    

class EditProduct(generic.UpdateView):
    model=Products
    form_class=AddProductForm
    context_object_name='product'
    template_name='myaccount/edit_product.html'
    success_url=reverse_lazy('myaccount')



class RemoveProductView(generic.DeleteView):
    model=Products
    form_class=AddProductForm
    context_object_name='product'
    template_name='myaccount/remove_product.html'
    success_url=reverse_lazy('myaccount')

class UpdateProfileIfo(generic.UpdateView):
    model=Profile
    form_class=CreateProfileForm
    template_name='myaccount/edit_profile.html'
    success_url=reverse_lazy('myaccount')
    


    



    