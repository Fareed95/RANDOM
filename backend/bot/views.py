# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BotResponse
from .serializers import BotResponseSerializer
from .bot_algo import bot_gemini

class BotResponseView(APIView):
    def get(self, request):
        bot_responses = BotResponse.objects.all()
        serializer = BotResponseSerializer(bot_responses, many=True)
        return Response(serializer.data)

    def post(self, request):
        question = request.data.get('question')
        if not question:
            return Response({'error': 'Question is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        bot_response_text = bot_gemini(question)
        bot_response = BotResponse.objects.create(question=question, bot_response=bot_response_text)
        serializer = BotResponseSerializer(bot_response)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
