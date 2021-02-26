from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.All, name='index'),
    url(r'^fa$', views.All, name='fa-index'),
    url(r'^sent$', views.sent, name='sent'),
    url(r'^', include('blog.urls')),
    # url(r'^', include('contact_page.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
