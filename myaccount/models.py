from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image1=models.ImageField(blank=True,null=True)
    image2=models.ImageField(blank=True,null=True)
    image3=models.ImageField(blank=True,null=True)
    image4=models.ImageField(blank=True,null=True)


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('myaccount')

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    whatsapp=models.CharField(max_length=255)
    phone1=models.CharField(max_length=255)
    phone2=models.CharField(max_length=255)
    phone3=models.CharField(max_length=255)
    profile_pic=models.ImageField(blank=True,null=True,upload_to='profile',default='static/images/avatar.png')

    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('myaccount')
   


