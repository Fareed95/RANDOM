from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import ResponseBotViewSet

# router = DefaultRouter()
# router.register('response',ResponseBotViewSet, basename='response' )


urlpatterns = [
    path('', ResponseBotViewset)
]
