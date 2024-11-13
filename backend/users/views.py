from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from django.utils import timezone
from .models import User
from .serializers import UserSerializer, PasswordResetRequestSerializer, PasswordResetSerializer
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.conf import settings
from social_django.utils import psa
from social_core.exceptions import AuthException
from django.shortcuts import redirect


# User model
User = get_user_model()

class RegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'OTP sent to your email. Please verify to complete registration.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def put(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        user = User.objects.filter(email=email).first()

        if user and user.otp == otp and user.otp_expiration > timezone.now():
            user.is_active = True
            user.otp = None
            user.otp_expiration = None
            user.save()
            return Response({'message': 'User verified successfully'})
        else:
            return Response({'error': 'Invalid OTP or OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User Not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        if not user.is_active:
            raise AuthenticationFailed('Account not activated. Please verify your email.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response

class LogoutView(APIView):
    @csrf_exempt
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': "Logged out successfully"
        }
        return response

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        otp = get_random_string(length=6, allowed_chars='0123456789')
        cache.set(f'otp_{email}', otp, timeout=300)  # OTP valid for 5 minutes

        send_mail(
            'Password Reset OTP',
            f'Your OTP for password reset is {otp}.',
            'nutriscanofficial@gmail.com',
            [email],
            fail_silently=False,
        )
        return Response({"message": "OTP sent to your email."}, status=status.HTTP_200_OK)

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        cached_otp = cache.get(f'otp_{email}')
        if cached_otp != otp:
            return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            cache.delete(f'otp_{email}')
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

class GoogleLoginView(APIView):
    @csrf_exempt
    def get(self, request):
        # Redirect to the Google OAuth2 authorization URL
        redirect_uri = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI
        google_auth_url = (
            f"https://accounts.google.com/o/oauth2/auth"
            f"?response_type=code"
            f"&client_id={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY}"
            f"&redirect_uri={redirect_uri}"
            f"&scope=email%20profile"
        )
        return redirect(google_auth_url)

    @csrf_exempt
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "No token provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Use `psa` (social-auth-app-django) to authenticate the token
            backend = 'social_core.backends.google.GoogleOAuth2'
            user = psa(backend).authenticate(request, access_token=token)
            
            if user is None:
                return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

            if not user.is_active:
                return Response({"error": "Account not activated"}, status=status.HTTP_401_UNAUTHORIZED)

            # Generate JWT token
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            response.data = {'jwt': jwt_token}

            return response

        except AuthException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
