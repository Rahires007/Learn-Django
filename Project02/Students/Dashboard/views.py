from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request,'Dashboard/Login.html')
def Signup(request):
    return render(request,'Dashboard/Signup.html')
def About(request):
    return render(request,'Dashboard/About.html')
def Contact(request):
    return render(request,'Dashboard/Contact.html')