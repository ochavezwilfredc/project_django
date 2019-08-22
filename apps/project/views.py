from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
