from django.urls import path
from .views import Login,Logout
urlpatterns=[
    path('',Login,name="Login"),
    path('Logout/',Logout,name="Logout")
]