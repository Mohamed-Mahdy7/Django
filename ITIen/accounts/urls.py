from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', Register.as_view(),name="register"),
]
