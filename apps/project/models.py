from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    address = models.TextField(blank=True, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Projecto"
        verbose_name_plural = "Projectos"
        ordering = ["-created"]

    def __str__(self):
        return self.name
