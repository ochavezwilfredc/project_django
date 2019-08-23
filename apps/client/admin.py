from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'telephone', 'email', 'image')
    ordering = ('name', 'telephone')
    search_fields = ('name', 'telephone', 'email')
    date_hierarchy = 'created'


# Register your models here.
admin.site.register(Client, ClientAdmin)
