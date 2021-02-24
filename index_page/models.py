from django.db import models


# Create your models here.

class IndexPage(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    site_address = models.URLField(max_length=150, null=True, blank=False)
    site_title = models.CharField(max_length=150, null=True, blank=False)
    job = models.CharField(max_length=150, null=False, blank=False)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    telegram = models.URLField(max_length=200, null=True, blank=True)
    git = models.URLField(max_length=200, null=True, blank=True)
    copyright = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    job = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.job
