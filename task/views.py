from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    
    context = {'tasks':tasks,'form':form}
    return render(request,'task/list.html',context)

def Update(request,pkey):
    task = Task.objects.get(id=pkey)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'form':form}
   
    return render(request,'task/update.html',context)

def Delete(request,pkey):
    item = Task.objects.get(id=pkey)

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    context = {'item':item}
    return render(request,'task/delete.html',context)