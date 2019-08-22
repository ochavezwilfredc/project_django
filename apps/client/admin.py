from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Register your models here.
admin.site.register(Client, ClientAdmin)
