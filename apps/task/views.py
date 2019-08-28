# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
