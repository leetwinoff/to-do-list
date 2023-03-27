from django.shortcuts import render
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task


def index(request):
    return render(request, "to_do_list/index.html")


class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/tasks.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
