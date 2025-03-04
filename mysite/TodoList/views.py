from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task
# Create your views here.

class TaskListView(generic.ListView):
    template_name = "TodoList/index.html"
    model = Task

class TaskDetailView(generic.DetailView):
    template_name = "TodoList/task_detail.html"
    model = Task

class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "TodoList/task_form.html"
    fields = '__all__'
    success_url = reverse_lazy('TodoList:index')

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "TodoList/task_delete.html"
    success_url = reverse_lazy('TodoList:index')

class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "TodoList/task_update.html"
    fields = '__all__'
    success_url = reverse_lazy('TodoList:index')
