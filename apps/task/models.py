from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    address = RichTextField(blank=True, verbose_name="Dirección")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Projecto"
        verbose_name_plural = "Projectos"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Activity(models.Model):
    STATES_ACTIVITY = (
        ('a', 'BORRADOR'),
        ('b', 'EN CURSO'),
        ('c', 'TERMINADA'),
    )
    name = models.CharField(max_length=100, verbose_name="Nombre de Actividad")
    state = models.CharField(verbose_name="Estado", max_length=1, choices=STATES_ACTIVITY, default='a')
    description = RichTextField(verbose_name="Descripción", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITIES = (
        ('alta', 'ALTA'),
        ('media', 'MEDIA'),
        ('baja', 'BAJA'),
    )
    name = models.CharField(max_length=200, verbose_name="Nombre de Tarea")
    responsible = models.ForeignKey(User, verbose_name="Responsable", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE)
    state = models.FloatField(verbose_name="Estado", default=0)
    priority = models.CharField(verbose_name="Prioridad", max_length=6, choices=PRIORITIES, default='alta')
    estimated_time = models.TimeField(verbose_name="Tiempo estimado")
    activities = models.ManyToManyField(Activity,
                                        verbose_name="Actividades", related_name="get_tasks")
    description = RichTextField(verbose_name="Descripción", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    # @priority
    # def get_activities_finished(self):
    #     pass

    @property
    def get_state_color(self):
        if 0 <= self.get_state() <= 25:
            return 'bg-danger '
        elif 25 < self.get_state() <= 75:
            return 'bg-warning'
        elif 75 < self.get_state() <= 100:
            return 'bg-success'

    def get_state(self):
        total = len(list(filter(lambda act: act.state == 'c', self.activities.all())))
        return round(((total / self.activities.count()) * 100), 2)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ('name',)

    def __str__(self):
        return self.name

# class ShowroomAdmin(admin.ModelAdmin):
#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if db_field.name == "activities":
#             kwargs["queryset"] = Activity.objects.filter(state='a')
#         return super(ShowroomAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
