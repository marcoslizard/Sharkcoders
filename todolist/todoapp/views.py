from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"task": tasks, "form": form}
    return render(request, "todo/index.html",context)

def deleteTask(request , pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("/")

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect("/")





