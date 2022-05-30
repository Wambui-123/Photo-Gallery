from django.urls import path
from .views import gallery_upload, index, gallery_create, gallery_update, gallery_delete
from . import views

app_name = 'gallery'

urlpatterns = [
        path('upload/', gallery_upload, name='gallery_upload'),
        path('index/', index, name='index'),
        # path('create/',LeadCreateView.as_view(), name='lead-create'),
        path('create/', gallery_create, name='gallery_create'),
        # path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
        # path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
        path('<int:pk>/update/', gallery_update, name='gallery_update'),
        # path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
        path('<int:pk>/delete/', gallery_delete, name='gallery_delete'),

]
