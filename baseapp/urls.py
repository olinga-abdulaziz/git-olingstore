from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('add/',views.add_view,name='add'),
    path('product_detail/<int:pk>/',views.ProductDetailView.as_view(),name='productdetail'),
    path('bycles/',views.CyclesList.as_view(),name='bycles'),
    path('clothing/',views.ClothingList.as_view(),name='clothing'),
    path('electronic/',views.ElectronList.as_view(),name='electronic'),
    path('farm/',views.FarmList.as_view(),name='farm'),
    path('housing/',views.HousinggList.as_view(),name='housing'),
    path('others/',views.OthersList.as_view(),name='others'),
    path('motobike/',views.MotobikeList.as_view(),name='motobike'),
    path('vehicles/',views.VehiclesList.as_view(),name='vehicles'),
    path('school/',views.SchoolView.as_view(),name='school'),
    path('search/',views.searchView,name='searches'),
    path('about/',views.aboutView,name='about'),
    path('contact/',views.contactView,name='contact'),
   
]
