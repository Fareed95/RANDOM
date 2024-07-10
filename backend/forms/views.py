from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Forms
from .serializers import FormsSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Okay backend is working properly")


@csrf_exempt
def FormsList(request):
    if request.method == "GET":
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms,many = True)
        return JsonResponse(serializer.data,safe=False)
