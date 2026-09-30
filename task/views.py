from django.shortcuts import render, redirect
from django.utils import timezone

from task.forms import TaskForm
from task.models import Task


def indexView(request):
    tasks = Task.objects.all()
    completed = Task.objects.filter(state=1)
    in_progress = Task.objects.filter(state=2)

    today = timezone.localdate()
    todays = Task.objects.filter(start_date__date=today)

    total_tasks = tasks.count()
    completed_tasks = completed.count()

    if total_tasks > 0:
        progress = round(completed_tasks / total_tasks * 100, 2)
    else:
        progress = 0

    if request.method == "POST":
        input_form = TaskForm(request.POST)
        if input_form.is_valid():
            input_form.save()
            return redirect('index')
    else:
        input_form = TaskForm()
    context = {
        'tasks': tasks,
        'completed': completed,
        'in_progress': in_progress,
        'todays': todays,
        'progress': progress,
        'input_form': input_form,
    }
    return render(request, 'task/index.html', context)

def editView(request,task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'task/edit.html',{'form':form})
    else:
        form = TaskForm(instance=task)
        return render(request,'task/edit.html',{'form':form})

def deleteView(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('index')
def toggleView(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.state == 1:
        task.state = 2
        task.save()
        return redirect('index')
    else:
        task.state = 1
        task.save()
        return redirect('index')
