from django.urls import path
from .views import *
urlpatterns=[
    path('Home/',Home),
    path('Welcome/',Welcome)
]