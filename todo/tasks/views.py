from django.shortcuts import get_object_or_404, redirect, render
from .models import MyTasks
from .forms import MyTaskForm
# Create your views here.

def home(request):
    allTasks = MyTasks.objects.all()
    taskForm = MyTaskForm()

    if request.method == 'POST':
        print(request.POST)
        if 'todo_button' in request.POST:
            addTask = MyTaskForm(request.POST)
            if addTask.is_valid():
                addTask.save()
        elif 'completed' in request.POST:
            task = MyTasks.objects.get(id=int(request.POST['id']))
            task.isComplete = not(task.isComplete)
            task.save()
        else:
            # print(request.POST)
            deletedTask = MyTasks.objects.get(id=int(request.POST['id']))
            deletedTask.delete()
        return redirect(home)
    context = {
        'allTasks': allTasks,
        'taskForm': taskForm,
    }
    return render(request, 'tasks/home.html', context)

def updateTask(request, task_id):
    task = get_object_or_404(MyTasks, id = task_id)
    if request.method == "POST":
        print(request.POST)
        if 'save' in request.POST:
            task.title = request.POST['title']
            if 'isComplete' in request.POST:
                if request.POST['isComplete'] == 'on':
                    task.isComplete = True
                else:
                    task.isComplete = False
            task.save()
        return redirect(home)
    context = {
        'task':task,
    }
    return render(request, 'tasks/update.html', context)