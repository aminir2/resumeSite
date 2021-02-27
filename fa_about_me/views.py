from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import *


# Create your views here.

class about_me(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        about = AboutPage.objects.first()
        doing_data = []
        doings = Doing.objects.all()
        for doing in doings:
            doing_data.append({
                'flag': doing.flag,
                'title': doing.title,
                'description': doing.description,
            })
        context = {
            'doing': doing_data,
            'about': about,
        }
        return render(request, 'fa-index.html', context)
