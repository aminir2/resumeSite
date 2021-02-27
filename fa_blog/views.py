from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import *
from fa_info.models import *


class Post(TemplateView):

    def get(self, request, *args, **kwargs):
        all_info = IndexPage.objects.first()
        all_jobs = Jobs.objects.all()
        post_id = kwargs['postID']
        post_data = []
        posts = BlogPost.objects.get_by_id(post_id)
        if posts is None or not posts.active:
            raise Http404('Page not found')
        context = {
            'setting_data': all_info,
            'jobs': all_jobs,
            'posts': posts
        }
        return render(request, 'fa-post.html', context)
