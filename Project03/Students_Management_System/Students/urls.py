from django.urls import path
from .views import *
urlpatterns=[
    path('Form/',Form),
    path('Dashboard/',Dashboard)
]