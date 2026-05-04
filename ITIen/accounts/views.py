from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'accounts/base.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    return render(request, 'accounts/logut.html')