from django.shortcuts import render
from .models import Students_Database
# Create your views here.
def Form(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        Class=request.POST.get("Class")
        City=request.POST.get("City")
        Students_Database.objects.create(Name=Name,Class=Class,City=City)
    return render(request,'Students/Form.html')
def Dashboard(request):
    Data=Students_Database.objects.all()
    return render(request,'Students/Dashboard.html',{"Data":Data})