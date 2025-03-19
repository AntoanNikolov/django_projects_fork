from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

###

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    #only show the update view when the logged in user matches the creator
    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerCreateView(LoginRequiredMixin, CreateView):
    #automatically assign the current user to the form
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    #only show the update view when the logged in user matches the creator
    def get_queryset(self):
        #the view in views.py will call the function in THIS class to update its queryset
        qs = super(OwnerDeleteView, self).get_queryset() 
        #owner is a field in the database which specifies the creator
        return qs.filter(owner=self.request.user) #filter the queryset so the owner must be the current user