from django.shortcuts import render
from django.views import generic
from .models import Service, TimeSlot

# Create your views here.

class ServicesView(generic.ListView):
    model = Service
    template_name = "Cosmetology/index.html"

class TimeSlotsView(generic.DetailView):
    model = TimeSlot
    template_name = "Cosmetology/timeslots.html"