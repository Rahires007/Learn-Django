from django.shortcuts import render
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