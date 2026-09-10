from django.urls import path
from .views import *
urlpatterns=[
    path('About/',About),
    path('Skills/',Skills),
    path('Contact/',Contact),
    path('Projects/',Projects)
]