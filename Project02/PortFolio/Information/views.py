from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request,'Information/About.html')
def Skills(request):
    return render(request,'Information/Skills.html')
def Contact(request):
    return render(request,'Information/Contact.html')
def Projects(request):
    return render(request,'Information/Projects.html')