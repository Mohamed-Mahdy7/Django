from django.shortcuts import render

# Create your views here.

def courseList(request):
    context = {
        "courses": [
            {"id": 1, "name": "Python"},
            {"id": 2, "name": "JS"},
            {"id": 3, "name": "Django"}
        ]
    }
    return render(request, "course/index.html", context)

def courseAdd(request):
    return render(request, "course/add.html")

def courseUpdate(request):
    return

def courseDelete(request):
    return