from django.urls import path

from apps.task.views import TaskListView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name="project_list"),
    path('', TaskListView.as_view(), name="task_list"),
]
