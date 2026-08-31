#For Documentation Readme.md
from django.urls import path
from .views import Greet,Welcome
urlpatterns=[
    path('Greet/',Greet),
    path('Welcome/',Welcome)
]