from django.urls import path
from .views import *
urlpatterns=[
    path('Form/',Form,name="Form"),
    path('Dashboard/',Dashboard,name="Dashboard")
]