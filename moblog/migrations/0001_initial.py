# Generated by Django 2.0.9 on 2018-11-18 21:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrendatario',
            fields=[
                ('rut_arrendatario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_arrendatario', models.CharField(max_length=40)),
                ('apellido_arrendatario', models.CharField(max_length=40)),
                ('correo_arrendatario', models.CharField(max_length=30)),
                ('telefono_arrendatario', models.CharField(max_length=30)),
                ('direccion_arrendatario', models.CharField(max_length=30)),
                ('comuna_arrendatario', models.CharField(max_length=15)),
                ('banco_arrendatario', models.CharField(blank=True, max_length=15, null=True)),
                ('n_cuenta_arrendatario', models.IntegerField(blank=True, null=True)),
                ('comuna_trabajo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('nombre_banco', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bici',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('annos_vida', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudadano_Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudadano_comuna', models.CharField(max_length=15)),
                ('trabajador_comuna', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente_banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_cliente', models.CharField(max_length=10)),
                ('n_cuenta_cliente', models.IntegerField(blank=True, null=True)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moblog.Banco')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('codigo_postal', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(choices=[('la reina', 'La reina'), ('ñuñoa', 'Nuñoa'), ('providencia', 'Providencia')], max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='ciudadano_comuna',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moblog.Comuna'),
        ),
    ]
