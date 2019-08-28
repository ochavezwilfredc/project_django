from ckeditor.fields import RichTextField
from django.db import models


class Reporter(models.Model):
    STATES_ACTIVITY = (
        ('A', 'BORRADOR'),
        ('B', 'EN CURSO'),
        ('C', 'TERMINADA'),
    )
    name = models.CharField(max_length=100, verbose_name="Nombre")
    # state_active = models.CharField(verbose_name="Estado", max_length=1, choices=STATES_ACTIVITY, default='A')
    description = RichTextField(verbose_name="Descripción", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return "%s %s" % (self.name, self.description)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
