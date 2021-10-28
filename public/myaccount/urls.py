from django.urls import path
from . import views

urlpatterns=[
    path('Myaccount/',views.MyProductView.as_view(),name='myaccount'),
    path('Add_new_product/',views.AddProduct.as_view(),name='addnewproduct'),
    path('create_profile/',views.CreateProfile.as_view(),name='createprofile'),
    path('Edit_product/<int:pk>/',views.EditProduct.as_view(),name='editproduct'),
    path('Edit_profile/<int:pk>/',views.UpdateProfileIfo.as_view(),name='editprofile'),
    path('Remove_product/<int:pk>/',views.RemoveProductView.as_view(),name='removeproduct'),
    
]