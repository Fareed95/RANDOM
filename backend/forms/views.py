from .models import Forms
from .serializers import  FormsSerializer
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet


def index(request):
    return HttpResponse("<h1 style = 'color: blue' class = 'nigga'>yes this nigga shiit is working</h1> ")
    
class Formslist(ModelViewSet):
    queryset = Forms.objects.all()
    serializer_class = FormsSerializer

