from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^fa$', views.Fa_All, name='fa-index'),
    url(r'^fa/sent$', views.sent, name='fa-sent'),
    url(r'^', include('index_page.urls')),
    url(r'^', include('blog.urls')),
    url(r'^', include('fa_blog.urls')),
    # url(r'^', include('contact_page.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
