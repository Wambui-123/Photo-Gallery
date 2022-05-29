from django.urls import path
from .views import gallery_upload, index
from . import views

app_name = 'gallery'

urlpatterns = [
        path('upload/', gallery_upload, name='gallery_upload'),
        path('index/', index, name='index'),

]
