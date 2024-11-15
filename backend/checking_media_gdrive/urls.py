# urls.py
from django.urls import path
from .views import ImageUploadView, ImageRetrieveView

urlpatterns = [
    path('upload-image/', ImageUploadView.as_view(), name='upload_image'),
    path('get-image/<str:file_id>/', ImageRetrieveView.as_view(), name='get_image'),
]
