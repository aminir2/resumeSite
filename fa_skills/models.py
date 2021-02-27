from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class CodeSkill(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت کدزنی'
        verbose_name_plural = 'مهارت کدزنی'


class DesignSkill(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت طراحی'
        verbose_name_plural = 'مهارت طراحی'


class Knowledge(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دانش'
        verbose_name_plural = 'دانش'


class Education(models.Model):
    year = models.CharField(max_length=50, null=False, blank=False)
    where = models.CharField(max_length=50, null=False, blank=False)
    what = models.CharField(max_length=50, null=False, blank=False)
    description = RichTextUploadingField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.what

    class Meta:
        verbose_name = 'تحصیل'
        verbose_name_plural = 'تحصیلات'


class Experience(models.Model):
    year = models.CharField(max_length=50, null=False, blank=False)
    where = models.CharField(max_length=50, null=False, blank=False)
    what = models.CharField(max_length=50, null=False, blank=False)
    description = RichTextUploadingField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.what

    class Meta:
        verbose_name = 'تجربه'
        verbose_name_plural = 'تجربیات'
