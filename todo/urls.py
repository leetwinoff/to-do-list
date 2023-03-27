from django.urls import path

from todo.views import index, TaskListView, TaskCreateView, TagListView, TaskUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tags-list"),
]

app_name = "todo"
