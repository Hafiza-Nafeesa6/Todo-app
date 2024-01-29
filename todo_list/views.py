from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializer import TodoSerializer


# Create your views here.
class TodoList(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer





