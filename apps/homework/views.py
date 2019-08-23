from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Homework


class HomeworkListView(ListView):
    model = Homework
    template_name = 'homework/homework_list.html'
    context_object_name = 'homeworks'
