from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Client
from .forms import ClientForm

from django.urls import reverse_lazy, reverse


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_form.html'
    fields = ('name', 'document', 'telephone', 'email', 'address', 'image')
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_update_form.html'


class ClientDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        """
        Redirect to the page listing all of the proxy urls
        """
        return reverse("client_list")

    def get(self, *args, **kwargs):
        """
        This has been overriden because by default
        DeleteView doesn't work with GET requests
        """
        return self.delete(*args, **kwargs)
