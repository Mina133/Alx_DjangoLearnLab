from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, FollowSerializer
from django.contrib.auth import get_user_model


User = get_user_model().objects.create_user
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
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = FollowSerializer
    pagination_class =[IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='follow')
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        if user_to_follow == request.user:
            return Response({'detail':f'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return Response({'detail':f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'], url_path='unfollow')
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = self.get_object()
        if user_to_unfollow == request.user:
            return Response({'detail':f'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(user_to_unfollow)
        return Response({'detail':f'You are no longer following {user_to_unfollow.username}'}, status=status.HTTP_200_OK)