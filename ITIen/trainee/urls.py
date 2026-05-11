from django.urls import path
from trainee.views import *

urlpatterns = [
    path('', TraineeList.as_view(), name="Trinee_list"),
    path('add/', TraineeAdd.as_view(), name="Trainee_add"),
    path('add-form/', TraineeAddGeneric.as_view(), name="Trainee_add_form"),
    path('details/<int:id>/', traineeDetails, name='Trainee_Details'),
    path('update/<int:id>/', traineeUpdate, name="Trainee_update"),
    path('delete/<int:id>/', traineeDelete, name="Trainee_delete"),
    path('delete-soft/<int:id>/', traineeSoftDelete, name="Trainee_delete_soft"),
    
]
