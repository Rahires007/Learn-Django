from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Employee_Management_System
# Create your views here.
def Dashboard(request):
    Employees=Employee_Management_System.objects.all()
    return render(request,'Employee/Dashboard.html',{"Employees":Employees})
def Form(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        City=request.POST.get("City")
        Salary=request.POST.get("Salary")
        Employee_Management_System.objects.create(Name=Name,City=City,Salary=Salary)
    return render(request,'Employee/Form.html')
def Delete(request,pk):
    Employee=get_object_or_404(Employee_Management_System,pk=pk)
    Employee.delete()
    return redirect(Dashboard)
def Update(request,pk):
    Employee=get_object_or_404(Employee_Management_System,pk=pk)
    if request.method=="POST":
        Name=request.POST.get("Name")
        City=request.POST.get("City")
        Salary=request.POST.get("Salary")
        Employee.Name=Name
        Employee.City=City
        Employee.Salary=Salary
        Employee.save()
        return redirect(Dashboard)
    else:
        return render(request,'Employee/Edit.html',{"Employee":Employee})