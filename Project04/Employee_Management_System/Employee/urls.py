from django.urls import path
from .views import *
urlpatterns=[
    path('',Dashboard,name="Dashboard"),
    path('Form/',Form,name="Form"),
    path('Delete/<int:pk>/',Delete,name="Delete"),
    path('Update/<int:pk>/',Update,name="Update")
]