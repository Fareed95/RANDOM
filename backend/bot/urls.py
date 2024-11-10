# urls.py
from django.urls import path
from .views import BotResponseView

urlpatterns = [
    path('bot_response/', BotResponseView.as_view(), name='bot_response'),
]
