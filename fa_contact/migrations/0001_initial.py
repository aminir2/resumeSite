# Generated by Django 3.1.7 on 2021-02-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('map_embeded', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'اطلاعات قسمت تماس باما',
                'verbose_name_plural': 'اطلاعات قسمت تماس باما',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'پیام دریافتی',
                'verbose_name_plural': 'پیام های دریافتی',
            },
        ),
    ]