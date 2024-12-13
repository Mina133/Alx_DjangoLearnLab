from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model().objects.create_user(username='test', password='test')
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': RegisterSerializer(user).data,
                'token': Token.objects.get(user=user).key
            })
        return Response(serializer.errors, status=400)
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                'user': UserSerializer(user).data,
                'token': serializer.validated_data['token']
            })
        return Response(serializer.errors, status=400)