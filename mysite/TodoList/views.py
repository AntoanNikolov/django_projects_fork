from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Task, Comment
# Create your views here.

class TaskListView(generic.ListView):
    template_name = "TodoList/index.html"
    model = Task

class TaskDetailView(generic.DetailView):
    template_name = "TodoList/task_detail.html"
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = Comment.objects.filter(task=self.object)
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
        comment = Comment(text=request.POST['comment'], task=t)
        comment.save()
        return redirect(reverse('TodoList:task_detail', args=[pk]))