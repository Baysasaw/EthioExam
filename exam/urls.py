from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.aboutus, name='About-US'),
    path('contact-as/', views.contactus, name='contact-us'),
    path('sign-in/', views.signin, name='signin'),
    path('sign-up', views.signup, name='sign-up')
]
