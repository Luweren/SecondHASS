from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from django.template import loader
from django.urls import reverse
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
        todo = ToDoList.objects.get(id=3)
        todo.item_set.create(text= request.POST['todoText'], deadline = request.POST['deadline'], progress = float(request.POST['progress']))
        todo.save()
        return HttpResponseRedirect(reverse('web:index'))
    except (KeyError, ToDoList.DoesNotExist):
        # redirect anyway
        return HttpResponseRedirect(reverse('web:index'))
        

def edit(request, item_id):
    try:
        todo = Item.objects.get(pk=item_id)
        context = {
            'todo': todo,
            'progress': todo.progress,
            'deadline': todo.deadline.strftime('%Y-%m-%d')
        }
    except Item.DoesNotExist:
        context = {}

    template = loader.get_template('web/edit.html')
    return HttpResponse(template.render(context, request))


def post_edit(request, item_id):
    try:
        todo = Item.objects.get(pk=item_id)
        todo.text = request.POST['todoText']
        todo.progress = request.POST['progress']
        todo.deadline = request.POST['deadline']
        todo.save()
        return HttpResponseRedirect(reverse('web:index'))
    except (KeyError, Item.DoesNotExist):
        # redirect anyway
        return HttpResponseRedirect(reverse('web:index'))


def post_delete(request, todo_id):
    try:
        todo = Item.objects.get(pk=todo_id)
        todo.delete()
        return HttpResponseRedirect(reverse('web:index'))
    except Item.DoesNotExist:
        # redirect anyway
        return HttpResponseRedirect(reverse('web:index'))
        