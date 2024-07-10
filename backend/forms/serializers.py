from . models import Forms 
from rest_framework import serializers

class FormsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone = serializers.IntegerField()
    email = serializers.EmailField( max_length=254)
    address = serializers.CharField( max_length=500)
