from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from .models import Task, Comment, Tag
from .forms import CommentForm
# Create your views here.

class TaskListView(generic.ListView):
    template_name = "TodoList/index.html"
    model = Task

class TaskDetailView(generic.DetailView):
    template_name = "TodoList/task_detail.html"
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = Comment.objects.filter(task=self.object).order_by('-updated_at')
        context['form'] = CommentForm()
        #context['tags'] = Tag.objects.filter(tag=self.object)

        return context

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

class CommentCreateView(View):
    def post(self, request, pk) :
        t = get_object_or_404(Task, id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = t
            comment.save()
        return redirect(reverse('TodoList:detail', args=[pk]))
    
class CommentDeleteView(View):
    def post(self, request, pk): #pk here is the primary key of the comment, not the task 
        c = get_object_or_404(Comment, id=pk) #grabbing that comment
        task_id = c.task.id #getting the task id to redirect properly
        c.delete()
        return redirect(reverse('TodoList:detail', args=[task_id]))

class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "TodoList/tag_form.html"
    fields = '__all__'
    success_url = reverse_lazy('TodoList:index')