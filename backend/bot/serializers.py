from rest_framework import serializers
from .models import BotResponse

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotResponse
        fields = ['id', 'question', 'bot_response']

class BotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotResponse
        fields = ['question']
