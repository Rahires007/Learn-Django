from django.urls import path
from .views import *
urlpatterns=[
    path('',Home),
    path('Register/',Register),
    path('Courses/',Course),
    path('Inquary/',Inquary)
]