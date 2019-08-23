from django.db import models
from django.contrib.auth.models import User


# from django.utils.timezone import now


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


# Create your models here.
class Task(models.Model):
    PRIORITIES = (
        ('alta', 'ALTA'),
        ('media', 'MEDIA'),
        ('baja', 'BAJA'),
    )
    name = models.CharField(max_length=200, verbose_name="Nombre de Tarea")
    responsible = models.ForeignKey(User, verbose_name="Responsable", on_delete=models.CASCADE, default="")
    state = models.FloatField(verbose_name="Estado")
    priority = models.CharField(verbose_name="Prioridad", max_length=6, choices=PRIORITIES, default='alta')
    estimated_time = models.TimeField(verbose_name="Tiempo estimado")
    description = models.TextField(verbose_name="Descripción", default="")
    activities = models.ManyToManyField(Activity,
                                        verbose_name="Actividades")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["-created"]

    def __str__(self):
        return self.name
