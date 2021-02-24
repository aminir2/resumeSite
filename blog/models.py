from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q


class PostManager(models.Manager):
    def get_active_posts(self):

        return self.get_queryset().filter(active=True)

    def get_by_id(self, postID):
        qs = self.get_queryset().filter(id=postID)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    url = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.title


# class BlogList(models.Model):
#     category = models.ManyToManyField(Category, null=False, blank=False)
#     date = models.CharField(max_length=20, null=False, blank=False)
#     title = models.CharField(max_length=20, null=False, blank=False)
#     image = models.ImageField(upload_to='blog/', null=False, blank=False)
#
#     def __str__(self):
#         return self.title


class BlogPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False, blank=False)
    description = RichTextUploadingField()
    date = models.CharField(max_length=20, null=False, blank=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/', null=True, blank=False)
    active = models.BooleanField(default=False)
    objects = PostManager()
    # image_list = models.ImageField(upload_to='blog/', null=True, blank=False)

    def get_absolute_url(self):
        return f"/post/{self.id}/{self.title.replace(' ', '-')}"

    def __str__(self):
        return self.title
