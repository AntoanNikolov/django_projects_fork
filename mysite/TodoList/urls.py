from django.urls import path

from . import views

app_name = "TodoList"
urlpatterns = [
    # ex: /TodoList/
    path("", views.TaskListView.as_view(), name="index"),
    # ex: /TodoList/5/
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("task_create", views.TaskCreateView.as_view(), name="create"),
    path("task_update/<int:pk>", views.TaskUpdateView.as_view(), name="update"),
    path("task_delete/<int:pk>", views.TaskDeleteView.as_view(), name="delete"),
    path("task/<int:pk>/comment_create", views.CommentCreateView.as_view(), name='comment_create'),
    path("comment_delete/<int:pk>", views.CommentDeleteView.as_view(), name='comment_delete'), #we only need the comment id here
    path("tag_list", views.TagListView.as_view(), name="tag_list"),
    path("tag_create", views.TagCreateView.as_view(), name="tag_create"),
    path("tag_delete/<int:pk>", views.TagDeleteView.as_view(), name="tag_delete"),
]
