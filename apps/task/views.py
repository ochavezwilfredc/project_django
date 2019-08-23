from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
