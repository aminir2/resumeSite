# Generated by Django 3.1.7 on 2021-02-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
