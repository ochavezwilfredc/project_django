from django.contrib import admin
from .models import Activity, Task


class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'state', 'priority', 'responsible')
    ordering = ('name', 'priority')
    search_fields = ('name', 'priority')
    date_hierarchy = 'created'
    # list_filter = ('responsible__username', 'activities__name',)

    def post_activities(self, obj):
        return ", ".join([c.name for c in obj.activities.all().order_by("name")])

    post_activities.short_description = "Actividades"


# Register your models here.
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Task, TaskAdmin)
