from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/index.html"
    ordering = ["is_done"]


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "to_do_list/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags-list")


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if not task.is_done:
        task.is_done = True
        task.save()
        return redirect('todo:task-list')
    else:
        task.is_done = False
        task.save()
        return redirect('todo:task-list')
