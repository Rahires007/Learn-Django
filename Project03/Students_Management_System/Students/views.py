from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
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
def Delete(request,pk):
    Student=get_object_or_404(Students_Database,pk=pk)
    Student.delete()
    return redirect(Dashboard)
def Update(request,pk):
    Student=get_object_or_404(Students_Database,pk=pk)
    if request.method=="POST":
        Name=request.POST.get("Name")
        Class=request.POST.get("Class")
        City=request.POST.get("City")
        Student.Name=Name
        Student.Class=Class
        Student.City=City
        Student.save()
        return redirect(Dashboard)
    else:
        return render(request,'Students/Edit.html',{"Student":Student})