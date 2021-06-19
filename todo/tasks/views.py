from django.shortcuts import get_object_or_404, redirect, render
from .models import MyTasks
from .forms import MyTaskForm
from user.models import User
# Create your views here.

def home(request, user_id):
    user = User.objects.get(user_id = user_id)
    allTasks = MyTasks.objects.filter(user_Obj = user)
    taskForm = MyTaskForm(initial = {'user_Obj':user})    #Initializing some members of the form with data
    # taskForm.user_id = user_id

    if request.method == 'POST':
        # print(request.POST)
        if 'todo_button' in request.POST:
            addTask = MyTasks()
            addTask.user_Obj = User.objects.get(user_id= user_id)
            addTask.title = request.POST['title']
            # addTask.user_id = user_id
            addTask.save()
        elif 'completed' in request.POST:
            task = MyTasks.objects.get(id=int(request.POST['id']))
            task.isComplete = not(task.isComplete)
            task.save()
        else:
            # print(request.POST)
            deletedTask = MyTasks.objects.get(id=int(request.POST['id']))
            deletedTask.delete()
        return redirect(home, user_id)
    context = {
        'allTasks': allTasks,
        'taskForm': taskForm,
    }
    return render(request, 'tasks/home.html', context)

def updateTask(request, task_id):
    task = get_object_or_404(MyTasks, id = task_id)
    user_id = task.user_Obj.user_id
    if request.method == "POST":
        print(request.POST)
        if 'save' in request.POST:
            task.title = request.POST['title']
            if 'isComplete' in request.POST:
                task.isComplete = True
            else:
                task.isComplete = False
            task.save()
        return redirect(home, user_id)
    context = {
        'task':task,
    }
    return render(request, 'tasks/update.html', context)