from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.

def courseList(request):
    context = {"courses":Course.objects.all()}
    return render(request, "course/course.html", context)

def courseDetails(request, id):
    context= {"course":Course.objects.get(pk=id)}
    return render(request, 'course/details.html', context)

def courseAdd(request):
    if request.method == "POST":
        Course.objects.create(
            name = request.POST["name"],
            code = request.POST["code"],
            track = request.POST["track"]
        )
        return redirect("Course_list")
    return render(request, "course/add.html")

def courseUpdate(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        course.name = request.POST.get("name")
        course.code = request.POST.get("code")
        course.track = request.POST.get("track")
        course.save()
        return redirect("Course_details", id=course.ID)
        
    return render(request, 'course/update.html', {"id": id})

def courseDelete(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        course.delete()
        return redirect("Course_list")
    
    return render(request, 'course/delete.html', {"id": id})
