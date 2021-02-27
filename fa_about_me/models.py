from django.db import models

# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class AboutPage(models.Model):
    About_me = RichTextUploadingField()
    age = models.CharField(max_length=5, null=False, blank=False)
    residence = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.About_me

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'


class Doing(models.Model):
    flag = models.CharField(max_length=20, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    description = RichTextUploadingField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کار های من'
        verbose_name_plural = 'کار های من'


class Doing2(models.Model):
    flag = models.CharField(max_length=20, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    description = RichTextUploadingField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کار های من'
        verbose_name_plural = 'کار های من'
