# Generated by Django 4.0.5 on 2022-06-09 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='deadline',
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]