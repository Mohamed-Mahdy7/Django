from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="Login"),
    path('register/', register,name="Register"),
    path('logout/', logout, name="Logout"),
]
