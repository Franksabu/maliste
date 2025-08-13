from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('index')

    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('index')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')
