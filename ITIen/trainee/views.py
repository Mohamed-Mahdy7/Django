from django.shortcuts import render
from .models import Trainee

# Create your views here.

def home(request):
    return render(request, "base.html")

def traineeList(request):
    context = {"students": Trainee.objects.all()}
    return render(request, "trainee/trainee.html", context)

def traineeDetails(request, id):
    context = {"student": Trainee.objects.get(pk=id)}
    return render(request, "trainee/details.html", context)

def traineeAdd(request):
    return render(request, "trainee/add.html")

def traineeUpdate(request, id):
    return render(request, "trainee/update.html", {"id": id})

def traineeDelete(request, id):
    return render(request, "trainee/delete.html", {"id": id})