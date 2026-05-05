from multiprocessing import context

from django.shortcuts import render
from .models import Course

# Create your views here.

def courseList(request):
    context = {"courses":Course.objects.all()}
    return render(request, "course/course.html", context)

def courseDetails(request, id):
    context= {"course":Course.objects.get(pk=id)}
    return render(request, 'course/details.html', context)

def courseAdd(request):
    return render(request, "course/add.html")

def courseUpdate(request, id):
    return render(request, 'course/update.html', {"id": id})

def courseDelete(request, id):
    return render(request, 'course/delete.html', {"id": id})