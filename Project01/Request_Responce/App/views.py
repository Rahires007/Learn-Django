from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Render Html Templates using Render 
def Home(request):
    return render(request,'App/Home.html')
#Render Message using HTTPResponce
def Welcome(request):
    return HttpResponse("Welcome")