from django.urls import path
from trainee.views import *

urlpatterns = [
    path('', traineeList, name="Trinee_list"),
    path('add/', traineeAdd, name="Trainee_add"),
    path('add-form/', traineeAddForm, name="Trainee_add_form"),
    path('details/<int:id>/', traineeDetails, name='Trainee_Details'),
    path('update/<int:id>/', traineeUpdate, name="Trainee_update"),
    path('delete/<int:id>/', traineeDelete, name="Trainee_delete"),
    path('delete-soft/<int:id>/', traineeSoftDelete, name="Trainee_delete_soft"),
    
]
