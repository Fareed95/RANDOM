from rest_framework.views import APIView
from django.http import HttpResponse
from .models import User
from . serializers import UserSerializer
from  rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


def index(request):
    return HttpResponse("hello world")

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status= status.HTTP_403_FORBIDDEN)
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        print(email)

        user = User.objects.filter(email=email).first()

        if user is None :
            raise AuthenticationFailed('User Not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload,'secret',algorithm='HS256')



        response = Response()

        response.set_cookie(key='jwt', value= token, httponly=True)
        response.data = {
            'jwt':token
        }


        return response
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')


        if not token :
            raise AuthenticationFailed('Unauthenticated!')
        
        try :
            payload = jwt.decode(token,'secret',algorithms="HS256")
        
        except :
            raise AuthenticationFailed('Unauthenticated!')
        

        user = User.objects.filter(id= payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : "logout succesfully"
        }
        return response


        