from django.urls import path
from .views import ImageView

urlpatterns = [
    # Change the URL pattern to accept a `file_id` in the path
    path('image/', ImageView.as_view(), name='image-list'),
    path('image/<str:file_id>/', ImageView.as_view(), name='image-detail'),  # for getting a specific image by file_id
]
