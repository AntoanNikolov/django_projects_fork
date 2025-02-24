from django.urls import path

from . import views

app_name = "Cosmetology"
urlpatterns = [
    # ex: /TodoList/
    path("", views.ServicesView.as_view(), name="index"),
    # ex: /TodoList/5/
    path("<int:pk>/", views.TimeSlotsView.as_view(), name="timeslots"),
]
