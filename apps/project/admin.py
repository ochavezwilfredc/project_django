from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'address')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
