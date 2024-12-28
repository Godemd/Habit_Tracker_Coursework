from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Используется для преобразования данных пользователя в формат JSON и обратно.

    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "telegram_id"]

    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и возвращает обычного пользователя с использованием email и пароля.

        """
        if not email:
            raise ValueError("Email обязателен для создания пользователя")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user