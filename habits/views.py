from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Habit
from .permissions import IsOwnerOrReadOnly
from .serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    """
    ViewSet для управления привычками.

    Методы:
        - list: Возвращает список всех привычек (личных и публичных).
        - retrieve: Возвращает конкретную привычку по ID.
        - create: Создает новую привычку.
        - update: Обновляет существующую привычку.
        - destroy: Удаляет привычку.

    Особенности:
        - Пользователь может видеть только свои привычки и публичные.
        - При создании привычки автоматически устанавливается текущий пользователь.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Возвращает queryset, фильтрующий привычки в зависимости от состояния аутентификации:
        - Аутентифицированные пользователи видят свои и публичные привычки.
        - Неаутентифицированные пользователи видят только публичные привычки.
        """
        if self.request.user.is_authenticated:
            return Habit.objects.filter(Q(user=self.request.user) | Q(is_public=True))
        return Habit.objects.filter(is_public=True)

    def perform_create(self, serializer):
        """
        Переопределяет создание объекта, чтобы автоматически привязать его к текущему пользователю.
        """
        serializer.save(user=self.request.user)


class PublicHabitListView(ListAPIView):
    """
    Представление для отображения только публичных привычек.

    """
    serializer_class = HabitSerializer

    def get_queryset(self):
        """
        Возвращает queryset с публичными привычками.
        """
        return Habit.objects.filter(is_public=True)


class UserHabitListView(ModelViewSet):
    """
    ViewSet для управления личными привычками пользователя.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращает queryset с привычками, принадлежащими текущему пользователю.
        """
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Переопределяет создание объекта, чтобы автоматически привязать его к текущему пользователю.
        """
        serializer.save(user=self.request.user)