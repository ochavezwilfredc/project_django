from django.contrib import admin

from .models import Reporter, Article


class ReporterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    # readonly_fields = ('first_name', 'last_name')
    list_display = ('headline', 'pub_date', 'reporter')


# Register your models here.
admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Article, ArticleAdmin)
