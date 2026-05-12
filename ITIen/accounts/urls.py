from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', home, name="home"),
    path('register/', Register.as_view(),name="register"),
]
