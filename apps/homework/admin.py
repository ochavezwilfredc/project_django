from django.contrib import admin
from .models import Activity, Homework


class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')


class HomeworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'responsible', 'priority', 'post_homeworks')
    ordering = ('responsible',)
    search_fields = ('title', 'responsible__username', 'activities__name',)
    date_hierarchy = 'created'
    list_filter = ('responsible__username', 'activities__name',)

    def post_homeworks(self, obj):
        return ", ".join([c.name for c in obj.activities.all().order_by("name")])

    post_homeworks.short_description = "Tareas"


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Homework, HomeworkAdmin)
