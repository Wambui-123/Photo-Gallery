from django.contrib import admin
from django.urls import path, include

from gallery_app.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page),
]
