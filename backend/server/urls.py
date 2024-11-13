from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("forms.urls")),
    path('api/', include('users.urls')),
    path('bot/',include('bot.urls')),
    path('checking/',include('checking_media_gdrive.urls')),
]
