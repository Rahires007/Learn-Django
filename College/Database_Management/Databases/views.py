from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    return render(request,'Database/Home.html')
def Register(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        Class=request.POST.get('Class')
        Course=request.POST.get('Course')
        Mentor=request.POST.get('Mentor')
        MobileNo=request.POST.get('MobileNo')
        Students_Details.objects.create(Name=Name,Class=Class,Course=Course,Mentor=Mentor,MobileNo=MobileNo)
    return render(request,'Database/Register.html')
def Course(request):
    Data=Courses.objects.all()
    return render(request,'Database/Courses.html',{'Courses':Data})
def Inquary(request):
    Data=Students_Details.objects.all()
    return render(request,'Database/Inquary.html',{'Inquaries':Data})