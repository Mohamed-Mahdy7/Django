from django.shortcuts import render, redirect
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
    if request.method == "POST":
        Trainee.objects.create(
            name = request.POST["name"],
            age = request.POST["age"],
            degree = request.POST["degree"]
        )
        return redirect('Trinee_list')
    return render(request, "trainee/add.html")

def traineeUpdate(request, id):
    trainee = Trainee.objects.get(pk=id)
    if request.method == "POST":
        trainee.name = request.POST.get("name")
        trainee.age = request.POST.get("age")
        trainee.degree = request.POST.get("degree")
        trainee.save()
        return redirect("Trainee_Details", id=trainee.ID)
    
    return render(request, "trainee/update.html", {"id": id})

def traineeDelete(request, id):
    trainee = Trainee.objects.get(pk=id)
    if request.method == "POST":
        trainee.delete()
        return redirect('Trinee_list')
    
    return render(request, 'trainee/delete.html')
