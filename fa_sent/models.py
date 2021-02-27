from django.db import models


# Create your models here.

class Send(models.Model):
    site_address = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.site_address

    class Meta:
        verbose_name = 'ادرس سایت فارسی'
        verbose_name_plural = 'ادرس سایت فارسی'
