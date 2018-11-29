# Generated by Django 2.0.9 on 2018-11-27 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('detalle', models.CharField(max_length=300)),
                ('imagen', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('Rescatado', 'rescatado'), ('Disponible', 'disponible'), ('Adoptado', 'adoptado')], max_length=20)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]