from django.urls import path

from . import views

app_name = "TodoList"
urlpatterns = [
    # ex: /TodoList/
    path("", views.TaskListView.as_view(), name="index"),
    # ex: /TodoList/5/
    path("<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
]
