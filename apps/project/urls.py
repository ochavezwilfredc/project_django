from django.urls import path

from apps.project.views import ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name="project_list"),
]
