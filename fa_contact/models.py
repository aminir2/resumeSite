from django.db import models


# Create your models here.

class ContactModel(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'پیام دریافتی'
        verbose_name_plural = 'پیام های دریافتی'


class ContactInfo(models.Model):
    location = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    map_embeded = models.CharField(max_length=600, blank=False, null=False)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'اطلاعات قسمت تماس باما'
        verbose_name_plural = 'اطلاعات قسمت تماس باما'
