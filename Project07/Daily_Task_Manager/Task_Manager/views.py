from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Task_Manager
# Create your views here.
def Home(request):
    All_Tasks=Task_Manager.objects.all()
    if request.method=="POST":
        Task=request.POST.get("Task")
        Task_Manager.objects.create(Task=Task)
    return render(request,'Task_Manager/Home.html',{"All":All_Tasks})
def Form(request):
    if request.method=="POST":
        Task=request.POST.get("Task")
        Task_Manager.objects.create(Task=Task)
    return render(request,'Task_Manager/Form.html')
def MarkAsDone(request,pk):
    Task=get_object_or_404(Task_Manager,pk=pk)
    Task.Status="Completed"
    Task.save()
    return redirect("http://127.0.0.1:8000/")
def Delete(request,pk):
    Task=get_object_or_404(Task_Manager,pk=pk)
    Task.delete()
    return redirect("http://127.0.0.1:8000/")
def MarkAsUndone(request,pk):
    Task=get_object_or_404(Task_Manager,pk=pk)
    Task.Status="Pending"
    Task.save()
    return redirect("http://127.0.0.1:8000/")
def Edit(request,pk):
    Task=get_object_or_404(Task_Manager,pk=pk)
    if request.method=="POST":
        NewTask=request.POST.get("Task")
        Task.Task=NewTask
        Task.save()
        return redirect(Home)
    else:
        return render(request,'Task_Manager/Edit.html',{"Task":Task})