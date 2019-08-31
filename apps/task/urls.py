from django.urls import path

from apps.task.views import TaskListView, ProjectListView
from apps.task.views import task_list

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('tests', task_list, name="test_list"),
    path('projects', ProjectListView.as_view(), name="project_list"),
]
