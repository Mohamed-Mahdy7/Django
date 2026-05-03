from django.urls import path
from course.views import *

urlpatterns = [
    path('', courseList, name="Course_list"),
    path('add/', courseAdd, name="Course_add")
]