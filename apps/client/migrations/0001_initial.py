# Generated by Django 2.2.4 on 2019-08-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre y Apellidos')),
                ('document', models.CharField(max_length=10, verbose_name='Documento')),
                ('telephone', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Dirección')),
                ('image', models.ImageField(blank=True, upload_to='clients', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created'],
            },
        ),
    ]
