from .models import Forms
from .serializers import  FormsSerializer, UsersSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def index(request):
    return HttpResponse("<h1 style = 'color: blue' class = 'nigga'>yes this nigga shiit is working</h1> ")
    
class Formslist(ModelViewSet):
    queryset = Forms.objects.all()
    serializer_class = FormsSerializer

    
    
class Userslist(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

