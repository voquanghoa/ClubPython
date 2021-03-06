# Generated by Django 2.1 on 2018-09-07 04:40

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_Add_location_time_for_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date_time',
            new_name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='update_time',
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
    ]
