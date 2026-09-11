from django.urls import path
from .views import Api_Create_View
urlpatterns=[
 path('Students/',Api_Create_View)   
]