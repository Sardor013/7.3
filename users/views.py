from django.shortcuts import render
from .models import User, Category
from rest_framework import viewsets
from .serializers import UserSerializer, CategorySerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer






