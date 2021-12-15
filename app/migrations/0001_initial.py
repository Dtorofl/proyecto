# Generated by Django 3.2.9 on 2021-12-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('horas', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField()),
                ('fecha', models.DateTimeField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.proyecto')),
            ],
        ),
    ]
