from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Todo


def index(request):
    return HttpResponse("Index")


def edit(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        context = {
            'todo': todo,
            'progress': int(todo.progress * 100),
            'deadline': todo.deadline.strftime('%Y-%m-%d')
        }
    except Todo.DoesNotExist:
        context = {}

    template = loader.get_template('web/edit.html')
    return HttpResponse(template.render(context, request))


def post_edit(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.todo_text = request.POST['todoText']
        todo.progress = int(request.POST['progress']) / 100
        todo.deadline = request.POST['deadline']
        todo.save()
        return HttpResponseRedirect(reverse('web:index'))
    except (KeyError, Todo.DoesNotExist):
        # redirect anyway
        return HttpResponseRedirect(reverse('web:index'))


def post_delete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return HttpResponseRedirect(reverse('web:index'))
    except Todo.DoesNotExist:
        # redirect anyway
        return HttpResponseRedirect(reverse('web:index'))
