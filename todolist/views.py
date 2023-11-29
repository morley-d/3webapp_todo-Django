from django.http import HttpResponse
from django.shortcuts import render
from todolist.models import ToDo

# Create your views here.


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})
