from django.urls import path

from todo.views import index, TaskListView, TaskCreateView

urlpatterns = [
    path("", index, name="index"),
    path("tasks", TaskListView.as_view(), name="task-list")
    path("tasks/create", TaskCreateView.as_view(), name="task-create")
]

app_name = "todo"
