from django.contrib import admin

from .models import Project, Activity, Task


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'address')


class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'state', 'description')


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'responsible', 'priority', 'project')

    ordering = ('responsible',)
    search_fields = ('name', 'responsible__username', 'activities__name',)
    date_hierarchy = 'created'
    list_filter = ('responsible__username', 'activities__name',)

    def post_tasks(self, obj):
        return ", ".join([a.name for a in obj.activities.all().order_by("name")])

    post_tasks.short_description = "Actividades"


admin.site.register(Project, ProjectAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Task, TaskAdmin)
