from django.urls import path

from apps.task.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
]
