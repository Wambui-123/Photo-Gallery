from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gallery_project.settings import STATIC_ROOT

from gallery.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('gallery/', include('gallery.urls') ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    