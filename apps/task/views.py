# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'


def task_list(request):
    queryset = Task.objects.all()
    context = {
        "name": "List",
        "task_list": queryset
    }
    return render(request, "task/test_list.html", context)
