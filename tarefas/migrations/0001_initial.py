# Generated by Django 4.2.5 on 2023-09-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('dt_criacao', models.DateField(auto_now_add=True)),
                ('dt_prevista', models.DateField()),
                ('dt_conclusao', models.DateField(null=True)),
            ],
        ),
    ]