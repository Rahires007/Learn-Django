from django.shortcuts import render
from .models import Students_Details
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Form(request):
    Students=Students_Details.objects.all()
    if request.method=="POST":
        Name=request.POST.get("Name")
        Class=request.POST.get("Class")
        City=request.POST.get("City")
        Students_Details.objects.create(Name=Name,Class=Class,City=City)
    return render(request,'Students/Form.html')
@login_required
def Dashboard(request):
    Students=Students_Details.objects.all()
    return render(request,'Students/Dashboard.html',{"Students":Students})