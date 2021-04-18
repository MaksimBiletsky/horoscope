from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import UserProfile
from .serializers import UserProfileSerializer


# Create your views here.


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        print(request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered new user'
            data['email'] = user.user.email
            data['username'] = user.user.username
            data['date_of_birth'] = user.date_of_birth
        else:
            data = serializer.errors
        return Response(data)


# class UserRegistration(generics.GenericAPIView):


