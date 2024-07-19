from django.shortcuts import render
from .models import Forms
from .serializers import Forms, FormsSerializer, UsersSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1 style = 'color: blue' class = 'nigga'>yes this nigga shiit is working</h1> ")
    
@api_view (['GET','POST'])
def Formslist(request):
    if request.method == 'GET':
        employee = Forms.objects.all()
        serializer = FormsSerializer(employee, many= True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = FormsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else :
            return Response(serializer.errors )
@api_view (['DELETE','GET','PUT'])
def FormsDetailView(request, pk):
    try:
        employee = Forms.objects.get(pk=pk)
    except Forms.DoesNotExist :
        return Response(status = 404)
    # print(employee)
    
    if request.method == "DELETE":
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        serializer = FormsSerializer(employee)
        return Response(serializer.data )
    elif request.method == "PUT":
        serializer = FormsSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else :
            return Response(serializer.errors )


@api_view(['GET','POST'])
def userlistview(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UsersSerializer(user, many =True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = UsersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else :
            return Response(serializer.errors )
        


@api_view (['DELETE','GET','PUT'])
def UsersDetailView(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist :
        return Response(status = 404)
    # print(employee)
    
    if request.method == "DELETE":
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        serializer = UsersSerializer(user)
        return Response(serializer.data )
    elif request.method == "PUT":
        serializer = UsersSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else :
            return Response(serializer.errors )