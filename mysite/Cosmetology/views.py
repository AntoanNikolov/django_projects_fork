from django.shortcuts import render
from django.views import generic
from .models import Services, TimeSlot

# Create your views here.

class ServicesView(generic.ListView):
    model = Services
    templatename = "Cosmetology/index.html"

class TimeSlotView(generic.ListView):
    model = TimeSlot
    templatename = "Cosmetology/timeslots.html"