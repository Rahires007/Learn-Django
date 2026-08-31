from django.urls import path
from .views import Login,Signup,About,Contact
urlpatterns=[
    path('Login/',Login),
    path('Signup/',Signup),
    path('About/',About),
    path('Contact/',Contact)
]