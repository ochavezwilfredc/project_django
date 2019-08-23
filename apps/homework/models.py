from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

# from django.utils.timezone import now
from apps.client.models import Client


class Activity(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de Actividad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Homework(models.Model):
    PRIORITIES = (
        ('alta', 'ALTA'),
        ('media', 'MEDIA'),
        ('baja', 'BAJA'),
    )
    title = models.CharField(max_length=200, verbose_name="Nombre de Tarea")
    responsible = models.ForeignKey(User, verbose_name="Responsable", on_delete=models.CASCADE, default="")
    state = models.FloatField(verbose_name="Estado")
    priority = models.CharField(verbose_name="Prioridad", max_length=6, choices=PRIORITIES, default='alta')
    estimated_time = models.TimeField(verbose_name="Tiempo estimado")
    description = RichTextField(verbose_name="Descripción", default="")
    activities = models.ManyToManyField(Activity,
                                        verbose_name="Actividades", related_name="get_homeworks")
    # activities = models.ForeignKey(Activity, related_name='activity', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["-created"]

    def __str__(self):
        return self.title
