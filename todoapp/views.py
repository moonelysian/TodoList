from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.utils.dateformat import DateFormat
from .models import Todo

def home(request):
    todos = Todo.objects.order_by('-id')
    now = datetime.today().date()
    return render(request, 'todo/home.html', {'todos':todos, 'now':now})

def detail(request, todo_id):
    todo_detail = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo/detail.html',{'todo':todo_detail})

def new(request):
    return render(request, 'todo/new.html')

def create(request):
    todo = Todo()
    todo.title = request.GET['title']
    todo.content = request.GET['content']
    todo.priority = request.GET['priority']
    todo.due = request.GET['due']
    if 'option' in request.GET:
        if todo.due is not None:
            todo.due = request.GET['due']
    todo.save()
    return redirect('/todo/' + str(todo.id))

def edit(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    if (request.method == 'POST'):
        todo.title = request.POST['title']
        todo.content = request.POST['content']
        todo.priority = request.POST['priority']
        todo.due = request.POST['due']
        todo.save()
        return redirect('/todo/'+str(todo.id))
    return render(request,'todo/edit.html', {'todo':todo} )

def destroy(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('/')

def check(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.check is False:
        todo.check = True
    else:
        todo.check =  False
    todo.save()
    return redirect('/')
