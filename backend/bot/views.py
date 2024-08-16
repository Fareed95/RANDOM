from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BotResponse
from .serializers import BotResponseSerializer
from .bot_algo import bot_gemini
from users.models import User
from django.shortcuts import get_object_or_404

class BotResponseView(APIView):
    def get(self, request):
        bot_responses = BotResponse.objects.all()
        serializer = BotResponseSerializer(bot_responses, many=True)
        return Response(serializer.data)

    def post(self, request):
        question = request.data.get('question')
        user_email = request.data.get('user_email')

        if not question:
            return Response({'error': 'Question is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not user_email:
            return Response({'error': 'User email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Lookup the user by email
        user = get_object_or_404(User, email=user_email)
        
        # Generate bot response with context
        bot_response_text = bot_gemini(question, user.id)
        
        # Create BotResponse instance associated with the user
        bot_response = BotResponse.objects.create(question=question, bot_response=bot_response_text, user=user)
        
        # Serialize the bot response
        serializer = BotResponseSerializer(bot_response)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
