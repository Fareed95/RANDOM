# serializers.py
from rest_framework import serializers
from .models import BotResponse

class BotResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotResponse
        fields = ['id', 'question', 'bot_response']
        read_only_fields = ['bot_response']
