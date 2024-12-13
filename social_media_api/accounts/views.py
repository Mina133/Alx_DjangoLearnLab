from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        bio = request.data.get('bio')
        profile_picture = request.data.get('profile_picture')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=400)

        user = CustomUser.objects.create_user(username=username, password=password, bio=bio, profile_picture=profile_picture)
        Token.objects.create(user=user)
        return Response({'detail': 'User created successfully'}, status=201)

class LoginView(APIView):
    permission_classes = [AllowAny]
    success_url = '/'

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=400)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    
