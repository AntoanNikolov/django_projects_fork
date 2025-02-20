from django.shortcuts import render
from django.views import generic
from .models import Task
# Create your views here.

class TaskListView(generic.ListView):
    template_name = "TodoList/index.html"
    model = Task

class TaskDetailView(generic.DetailView):
    template_name = "TodoList/task_detail.html"
    model = Task