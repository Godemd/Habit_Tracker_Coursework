from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.

    Используется для преобразования данных привычки в формат JSON и обратно.

    Атрибуты:
        user: Поле, автоматически заполняемое текущим пользователем.
    
    Класс Meta:
        model: Указывает модель Habit, которую сериализует данный класс.
        fields: Список полей модели, которые будут включены в сериализованный вывод.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = (
            'id', 
            'user',
            'action',
            'place', 
            'time',
            'is_pleasant',
            'linked_habit',
            'reward',
            'period',
            'duration',
            'is_public'
        )
