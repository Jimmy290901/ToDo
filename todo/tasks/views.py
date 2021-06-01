from django.shortcuts import render
from .models import MyTasks
from .forms import MyTaskForm
# Create your views here.

def home(request):
    allTasks = MyTasks.objects.all()
    taskForm = MyTaskForm()

    if request.method == 'POST':
        addTask = MyTaskForm(request.POST)
        if addTask.is_valid():
            addTask.save()

    context = {
        'allTasks': allTasks,
        'taskForm': taskForm,
    }
    return render(request, 'tasks/home.html', context)