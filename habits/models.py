from django.contrib.auth import get_user_model
from django.db import models

from .validators import validate_habit_fields

User = get_user_model()

class Habit(models.Model):
    """
    Модель для управления привычками пользователя.

    Атрибуты:
        user: Связь с пользователем, создавшим привычку.
        action: Описание действия, связанного с привычкой.
        place: Место выполнения привычки.
        time: Время выполнения привычки.
        is_pleasant: Флаг, указывающий, является ли привычка приятной.
        linked_habit: Ссылка на другую связанную привычку.
        reward: Вознаграждение за выполнение привычки.
        period: Периодичность выполнения (в днях).
        duration: Длительность выполнения привычки (в секундах).
        is_public: Флаг, указывающий, является ли привычка публичной.
    """

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="habits", 
        verbose_name="Создатель"
    )
    action = models.CharField(max_length=255, verbose_name="Действие")
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время выполнения")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    linked_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"is_pleasant": True},
        verbose_name="Связанная привычка",
    )
    reward = models.CharField(max_length=255, blank=True, verbose_name="Вознаграждение")
    period = models.PositiveSmallIntegerField(default=1, verbose_name="Периодичность (в днях)")
    duration = models.PositiveIntegerField(verbose_name="Время на выполнение (в секундах)")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    class Meta:
        """
        Метаданные модели Habit.

        Атрибуты:
            verbose_name: Человекочитаемое имя модели в единственном числе.
            verbose_name_plural: Человекочитаемое имя модели во множественном числе.
            ordering: Порядок сортировки записей по умолчанию.
        """
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ['-id']  # Сортировка по убыванию id

    def __str__(self):
        """
        Возвращает строковое представление привычки.
        """
        return f"{self.action} ({'Публичная' if self.is_public else 'Личная'})"

    def save(self, *args, **kwargs):
        """
        Сохраняет объект в базе данных после валидации полей.

        Вызывает кастомный валидатор для проверки данных перед сохранением.
        """
        validate_habit_fields(self)
        super().save(*args, **kwargs)
