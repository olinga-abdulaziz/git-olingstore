from django.urls import path
from .import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import MyPasswordsChangeView,MyPasswordsChangeDoView

urlpatterns =[
    path('register/',views.RegisterView.as_view(),name='register'),
    path('edit/',views.EditView.as_view(),name='edit'),
    path('password/',MyPasswordsChangeView.as_view(),name='password'),
    path('password_change/done/',MyPasswordsChangeDoView.as_view(),name='done')
]