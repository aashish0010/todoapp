from django.shortcuts import render,redirect
from .models import todo

# Create your views here.
def home(request):
    data = todo.objects.all()
    return render(request,'home.html',{'data':data})

# adding todo
def add(request):
    tododata=request.POST['todo']
    todo_item =todo(content=tododata)
    todo_item.save()
    return redirect(home)

# deleting todo
def delete(request, todo_id):
    item = todo.objects.get(id=todo_id)
    item.delete()
    return redirect(home)