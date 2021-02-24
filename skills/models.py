from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class CodeSkill(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title


class DesignSkill(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title


class Knowledge(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Education(models.Model):
    year = models.CharField(max_length=50, null=False, blank=False)
    where = models.CharField(max_length=50, null=False, blank=False)
    what = models.CharField(max_length=50, null=False, blank=False)
    description = RichTextUploadingField(max_length=200, null=False, blank=False)


    def __str__(self):
        return self.what


class Experience(models.Model):
    year = models.CharField(max_length=50, null=False, blank=False)
    where = models.CharField(max_length=50, null=False, blank=False)
    what = models.CharField(max_length=50, null=False, blank=False)
    description = RichTextUploadingField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.what
