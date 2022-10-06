from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

class ListViewApi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class CreateViewApi(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class UpdateViewApi(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class DestroyViewApi(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer