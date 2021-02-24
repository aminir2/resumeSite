# Generated by Django 3.1.7 on 2021-02-23 23:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_education_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=200),
        ),
    ]
