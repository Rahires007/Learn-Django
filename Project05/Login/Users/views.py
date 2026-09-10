from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Login(request):
    if request.method=="POST":
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        User=authenticate(request,username=Username,password=Password)
        if User is not None:
            login(request,User)
            return redirect("Dashboard")
        else:
            return redirect("Login")

    return render(request,'Users/Login.html')
def Logout(request):
    logout(request)
    return redirect("Login")