from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def tables(response, id):
    ls= ToDoList.objects.get(id=id)
    return render(response, "testapp/index.html",{"ls":ls})
def index(response):
    ls= ToDoList.objects.get(id=3)
    return render(response, "testapp/index.html",{"ls":ls})
def create(response):
    return render(response, "testapp/create.html",{})
def impressum(response):
    return render(response, "testapp/Impressum.html",{})
def howto(response):
    return render(response, "testapp/HowTo.html",{})
    
def post_create(request):
    try:
        todo = ToDo.objects.get(pk=todo_id)
        todo.todo_text = request.POST['todoText']
        todo.progress = float(request.POST['progress'])
        todo.deadline = request.POST['deadline']
        todo.save()
        return HttpResponseRedirect(reverse('web:index'))
    except (KeyError, Todo.DoesNotExist):
        # redirect anyway
        return HttpResponseRedirect(reverse('web:index'))
        