from django.urls import path

from . import views

app_name = "TodoList"
urlpatterns = [
    # ex: /TodoList/
    path("", views.TaskListView.as_view(), name="index"),
    # ex: /TodoList/5/
    path("<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("task_create", views.TaskCreateView.as_view(), name="create"),
    path("task_update/<int:pk>", views.TaskUpdateView.as_view(), name="update"),
    path("task_delete/<int:pk>", views.TaskDeleteView.as_view(), name="delete"),
    path("<int:pk>/comment_create", views.CommentCreateView.as_view(), name='comment_create'),
]
