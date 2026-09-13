from django.urls import path
from .views import *
urlpatterns=[
    #Home
    path('',Home,name="Home"),
    #Add Task
    path('Form/',Form),
    #Mark As Done
    path('MarkAsDone/<int:pk>/',MarkAsDone,name="MarkAsDone"),
    #Delete
    path('Delete/<int:pk>/',Delete,name="Delete"),
    #Mark as UnDone
    path('MarkAsUndone/<int:pk>/',MarkAsUndone,name="MarkAsUndone"),
    #Edit 
    path('Edit/<int:pk>/',Edit,name="Edit")
]