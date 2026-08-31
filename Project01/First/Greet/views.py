from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def Greet(request):
    return HttpResponse("Hello Friends....") 
def Welcome(request):
    return HttpResponse("Welcome Friends...")
