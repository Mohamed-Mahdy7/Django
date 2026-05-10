from django.shortcuts import render, redirect
from .models import Trainee
from course.models import Course
from .forms import TraineeForm, TraineeFormModel

# Create your views here.

def home(request):
    return render(request, "base.html")

def traineeList(request):
    context = {"trainees": Trainee.objects.filter(is_active=True)}
    return render(request, "trainee/trainee.html", context)

def traineeDetails(request, id):
    context = {"trainee": Trainee.objects.get(pk=id)}
    return render(request, "trainee/details.html", context)

def traineeAdd(request):
    context = {"trainees": Trainee.objects.all(), 'form':TraineeFormModel()}
    if request.method == "POST":
        form = TraineeFormModel(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Trinee_list')
    return render(request, "trainee/add.html", context=context)

def traineeAddForm(request):
    context = {"trainees": Trainee.objects.all(), 'form':TraineeForm()}
    if request.method == "POST":
        form = TraineeForm(data=request.POST, files=request.FILES)        
        if form.is_valid():
            print("\nTHIS IS VALID\n")
            Trainee.objects.create(
            name = request.POST["name"],
            age = request.POST["age"],
            degree = request.POST["degree"],
            image = request.FILES["image"],
            course = Course.objects.get(
                pk=request.POST["course"]
            ))
            return redirect('Trinee_list')
        else:
            print(form.errors)
    return render(request, "trainee/add.html", context=context)

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

def traineeSoftDelete(request, id):
    trainee = Trainee.objects.get(pk=id)
    if request.method == "POST":
        trainee.is_active = False
        trainee.save()
        return redirect('Trinee_list')
    return render(request, 'trainee/delete.html')
