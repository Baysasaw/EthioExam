from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutus, name='about'),
    path('contact-as/', views.contactus, name='contactus'),
    path('sign-in/', views.signin, name='sign_in'),
    path('sign-up', views.signup, name='sign_up')
]
