from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from .models import Task, Comment, Tag
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from TodoList.owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView
# Create your views here.

class TaskListView(generic.ListView):
    template_name = "TodoList/index.html"
    model = Task

class TaskDetailView(generic.DetailView):
    template_name = "TodoList/task_detail.html"
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = Comment.objects.filter(task=self.object).order_by('-updated_at') #doing this here instead of in DTL to order them
        context['form'] = CommentForm()

        return context

class TaskCreateView(OwnerCreateView):
    model = Task
    template_name = "TodoList/task_form.html"
    fields = ['task_summary', 'task_details', 'tags']
    success_url = reverse_lazy('TodoList:index')

class TaskDeleteView(OwnerDeleteView):
    model = Task
    template_name = "TodoList/task_delete.html"
    success_url = reverse_lazy('TodoList:index')

class TaskUpdateView(OwnerUpdateView):
    model = Task
    template_name = "TodoList/task_update.html"
    fields = ['task_summary', 'task_details', 'tags']
    success_url = reverse_lazy('TodoList:index')

class CommentCreateView(LoginRequiredMixin, View):
    #LoginRequiredMixin attempted to redirect to a GET method in the CommentCreateView after the user logs in
    #This does not work, since we do not want a GET method here, so we make a fake one
    #so that LoginRequiredMixin actually redirects back to the detail page upon login
    #strange solution but it works ¯\_(ツ)_/¯
    def get(self,request,pk):
        return redirect(reverse('TodoList:detail', args=[pk]))
    
    def post(self, request, pk) :
        t = get_object_or_404(Task, id=pk) #grab our current task
        form = CommentForm(request.POST) #store the post data in the form into this variable
        if form.is_valid():
            comment = form.save(commit=False) #use the form variable to modify parameters of new comment
            comment.task = t #assign the correct task foreign key
            comment.owner = self.request.user
            comment.save() #save that thang
        return redirect(reverse('TodoList:detail', args=[pk]))
    
class CommentDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):  #pk is the comment id
        #using the comment to get the associated task ID, explanation for all this madness is above
        comment = get_object_or_404(Comment, id=pk)
        task_id = comment.task.id
        return redirect(reverse('TodoList:detail', args=[task_id]))

    def post(self, request, pk): #pk here is the primary key of the comment, not the task 
        c = get_object_or_404(Comment, id=pk, owner=self.request.user) #grabbing that comment
        task_id = c.task.id #getting the task id to redirect properly
        c.delete()
        return redirect(reverse('TodoList:detail', args=[task_id]))

class TagListView(generic.ListView):
    template_name = "TodoList/tag_list.html"
    model = Tag


class TagCreateView(OwnerCreateView):
    model = Tag
    template_name = "TodoList/tag_form.html"
    fields = ['text']
    success_url = reverse_lazy('TodoList:tag_list')

class TagDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return redirect(reverse('TodoList:tag_list'))
    
    def post(self, request, pk): 
        t = get_object_or_404(Tag, id=pk, owner=self.request.user) #we can just do this here cause we are not using generic
        t.delete()
        return redirect(reverse('TodoList:tag_list'))