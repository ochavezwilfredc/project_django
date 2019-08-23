from django.urls import path

from apps.client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('', ClientListView.as_view(), name="client_list"),
    path('task-new/', ClientCreateView.as_view(), name="client_new"),
    path('<int:pk>/task-update/', ClientUpdateView.as_view(), name="client_update"),
    # path('<int:pk>/task-delete/', ClientDeleteView.as_view(), name="client_delete"),
]
