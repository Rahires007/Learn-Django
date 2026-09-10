from django.urls import path
from .views import *
urlpatterns=[
    path('',Dashboard),
    path('Form/',Form)
]