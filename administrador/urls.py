"""administrador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

from apps.core import views as core_views
from apps.client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView
from apps.project.views import ProjectListView

urlpatterns = [
    path('', core_views.home, name='home'),

    # Urls de cliente
    path('client-list/', ClientListView.as_view(), name="client_list"),
    path('client-new/', ClientCreateView.as_view(), name="client_new"),
    path('<int:pk>/client-update/', ClientUpdateView.as_view(), name="client_update"),
    # path('<int:pk>/client-delete/', ClientDeleteView.as_view(), name="client_delete"),

    # Urls de proyectos
    path('project-list/', ProjectListView.as_view(), name="project_list"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
