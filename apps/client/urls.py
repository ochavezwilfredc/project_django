from django.urls import path

from apps.client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('', ClientListView.as_view(), name="client_list"),
    path('homework-new/', ClientCreateView.as_view(), name="client_new"),
    path('<int:pk>/homework-update/', ClientUpdateView.as_view(), name="client_update"),
    # path('<int:pk>/homework-delete/', ClientDeleteView.as_view(), name="client_delete"),
]
