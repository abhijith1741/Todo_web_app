from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Task
from . forms import TaskForm
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        priority=request.POST['priority']
        task=Task(name=name,priority=priority)
        task.save()
    obj = Task.objects.order_by('-id')
    return render(request,'home.html',{'obj':obj})

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def update(request,id):
    obj=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form})
