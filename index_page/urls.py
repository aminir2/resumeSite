from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.All, name='index'),
    url(r'^sent$', views.sent, name='sent'),

]
