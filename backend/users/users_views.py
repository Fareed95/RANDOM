# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.exceptions import AuthenticationFailed
# import jwt
# import datetime
# from . models import User
# from . serializers import UserSerializer


# # @method_decorator(csrf_exempt, name='dispatch')
# class UserView(APIView):
#     @csrf_exempt
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms="HS256")
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Token expired!')
#         except jwt.InvalidTokenError:
#             raise AuthenticationFailed('Invalid token!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)

#         return Response(serializer.data)
