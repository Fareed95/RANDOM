from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Forms
from .serializers import FormsSerializer
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
    return HttpResponse("Okay backend is working properly")


@csrf_exempt
def FormsList(request):
    if request.method == "GET":
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms,many = True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = FormsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)