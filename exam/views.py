from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'exam/Home.html')

def signin(request):
    return render(request, 'exam/signin.html')

def signup(request):
    return render(request, 'exam/sign_up.html')

def contactus(request):
    return render(request, 'exam/contactus.html')

def aboutus(request):
    return render(request, 'exam/Aboutus.html')



