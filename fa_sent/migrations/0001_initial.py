# Generated by Django 3.1.7 on 2021-02-27 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_address', models.URLField()),
            ],
            options={
                'verbose_name': 'ادرس سایت فارسی',
                'verbose_name_plural': 'ادرس سایت فارسی',
            },
        ),
    ]
