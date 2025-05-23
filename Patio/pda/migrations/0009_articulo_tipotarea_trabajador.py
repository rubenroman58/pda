# Generated by Django 5.1.7 on 2025-04-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pda', '0008_paquete_horafin_paquete_horainicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
