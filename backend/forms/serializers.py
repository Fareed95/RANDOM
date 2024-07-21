from rest_framework import serializers
from .models import Forms
# from django.contrib.auth.models import User


class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = '__all__'


# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User 
#         fields = '__all__'
