from rest_framework import serializers
from .models import User
from django.core.mail import send_mail
import random
import datetime
from django.utils import timezone
from bot.models import BotResponse
from bot.serializers import BotResponseSerializer

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    otp = serializers.CharField(write_only=True, required=False)
    botresponse = BotResponseSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password', 'otp','botresponse']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)
        
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})

        return data

    def create(self, validated_data):
        otp = str(random.randint(1000, 9999))
        validated_data['otp'] = otp
        validated_data['otp_expiration'] = datetime.datetime.now() + datetime.timedelta(minutes=10)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Send email with OTP
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            'nutriscanofficial@gmail.com',  # Replace with your email
            [validated_data['email']],
            fail_silently=False,
        )

        return user


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
