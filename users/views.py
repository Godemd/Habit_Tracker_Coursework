from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer


from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserCreateAPIView(CreateAPIView):
    """
    Представление для создания нового пользователя.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Представление для получения токенов доступа и обновления с использованием JWT.

    """
    pass


class ProfileViewSet(ViewSet):
    """
    Представление для получения профиля пользователя.

    """
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        """
        Получает информацию о пользователе по его ID (pk).
        
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
