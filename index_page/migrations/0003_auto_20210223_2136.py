# Generated by Django 3.1.7 on 2021-02-23 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0002_jobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='job1',
            new_name='job',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='job2',
        ),
    ]
