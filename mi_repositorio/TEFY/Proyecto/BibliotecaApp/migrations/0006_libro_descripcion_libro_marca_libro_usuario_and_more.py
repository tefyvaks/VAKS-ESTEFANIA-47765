# Generated by Django 4.2.5 on 2023-10-30 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BibliotecaApp', '0005_pelicula_delete_socio'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(default='Sin descripción disponible'),
        ),
        migrations.AddField(
            model_name='libro',
            name='marca',
            field=models.CharField(default='Desconocida', max_length=50),
        ),
        migrations.AddField(
            model_name='libro',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='libro',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]