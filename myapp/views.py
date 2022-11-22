from django.http import HttpResponse, JsonResponse   
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import createNewTask


# Create your views here.
def index(request):
    title = "Inicio de la pagina"
    return render(request, 'index.html', {
        'title' : title
    })

def about(request):
    return render(request, 'about.html')

def hello(request, id):
    result = id + 100 * 2
    return HttpResponse("<h1>Hello %s</h1>" %result)



def projects(request):
    # projects = list(Project.objects.values())
    projects = list(Project.objects.all())
    return render(request, 'projects.html', {
        'projects' : projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    task = list(Task.objects.all())
    return render(request, 'tasks.html', {
        'task' : task
    })   

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
        'form':createNewTask()
    })
    else:
        Task.objects.create(title=request.POST['title'],
        descripcion=request.POST['descripcion'], project_id=1)
        return redirect('/tasks/')
            