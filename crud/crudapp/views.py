from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index (request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'index.html', {'todos' : todos, 'form': form})

def update(request, pk):
    todo = Todo.objects.get(id = pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')    
    return render(request, 'update.html', {'form': form, 'todo': todo})

def delete(request, pk):
    todo = Todo.objects.get(id = pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'delete.html', {'todo': todo})