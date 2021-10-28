from django import forms
from myaccount.models import Products,Profile

categories =[('Electronics','Electronics'),('Clothings','Clothings'),('Vehicles','Vehicles'),('Motorbikes','Motorbikes'),('Bycles','Bycles'),('Farming','Farming'),('Housing','Housing'),('School','School'),('Health','Health'),('Tools','Tools'),('Others','Others')]
class AddProductForm(forms.ModelForm):
    class Meta:
         model=Products
         fields=("product_name","category","price","quantity","user","address","description","image1","image2","image3","image4")

         widgets = {
             "product_name":forms.TextInput(attrs={'class':'form-control'}),
             "category":forms.Select(choices=categories, attrs={'class':'form-control'}),
             "price":forms.TextInput(attrs={'class':'form-control'}),
             "quantity":forms.TextInput(attrs={'class':'form-control'}),
             "user":forms.TextInput(attrs={'class':'form-control','id':'user','type':'hidden'}),
             "address":forms.TextInput(attrs={'class':'form-control'}),
             "description":forms.Textarea(attrs={'class':'form-control'}),
             "image1":forms.FileInput(attrs={'class':'file-control'}),
             "image2":forms.FileInput(attrs={'class':'file-control'}),
             "image3":forms.FileInput(attrs={'class':'file-control'}),
             "image4":forms.FileInput(attrs={'class':'file-control'}),
         }

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile

        fields=("user","whatsapp","phone1","phone2","phone3","profile_pic")
        
        widgets = {
             "user":forms.TextInput(attrs={'class':'form-control','id':'user','type':'hidden'}),
             "whatsapp":forms.TextInput(attrs={'class':'form-control'}),
             "phone1":forms.TextInput(attrs={'class':'form-control'}),
             "phone2":forms.TextInput(attrs={'class':'form-control'}),
             "phone3":forms.TextInput(attrs={'class':'form-control'}),
             "profile_pic":forms.FileInput(attrs={'class':'file-control'}),
         }

