from django.urls import path

from apps.homework.views import HomeworkListView

urlpatterns = [
    path('', HomeworkListView.as_view(), name="homework_list"),
]
