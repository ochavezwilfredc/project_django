from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre y Apellidos")
    document = models.CharField(max_length=10, verbose_name="Documento")
    telephone = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo")
    address = models.CharField(blank=True, max_length=250, verbose_name="Dirección")
    image = models.ImageField(blank=True, verbose_name="Imagen", upload_to="clients")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-created"]

    def __str__(self):
        return self.name
