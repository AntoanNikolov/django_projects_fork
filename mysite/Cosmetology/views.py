from django.shortcuts import render
from django.views import generic
from .models import Service, TimeSlot

# Create your views here.

class ServicesView(generic.ListView):
    model = Service
    template_name = "Cosmetology/index.html"

#we are making a detail view which also serves as a list view. The timeslots of one service are details of the service but 
#they are objects that need to be listed
class ServiceTimeSlotsView(generic.DetailView):
    model = Service
    template_name = "Cosmetology/timeslots.html"
    context_object_name = "service"  #so we can use {{ service }} in the template (https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #show only time slots for this service that are not occupied.
        #context['timeslots'] = TimeSlot.objects.filter(service=self.object, is_occupied=False)
        context['timeslots'] = TimeSlot.objects.filter(service=self.object)
        return context