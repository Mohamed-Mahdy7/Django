from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "base.html")

def traineeList(request):
    context = {
        "students": [
            {"id": 1, "name": "ahmed"},
            {"id": 2, "name": "mohamed"},
            {"id": 3, "name": "omar"}
        ]
    }
    return render(request, "trainee/trainee.html", context)

def traineeAdd(request):
    return render(request, "trainee/add.html")

def traineeUpdate(request, id):
    return render(request, "trainee/update.html", {"id": id})

def traineeDelete(request, id):
    return render(request, "trainee/delete.html", {"id": id})