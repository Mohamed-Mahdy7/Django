from django.urls import path
from course.views import *

urlpatterns = [
    path('', courseList, name="Course_list"),
    path('add/', courseAdd, name="Course_add"),
    path('update/<int:id>/', courseUpdate, name="Course_update"),
    path('delete/<int:id>/', courseDelete, name="Course_delete"),
    
]