from django.apps import AppConfig

class HabitsConfig(AppConfig):
    """
    Класс конфигурации для приложения 'habits'.

    Этот класс определяет настройки по умолчанию для приложения 'habits',
    включая тип автоинкрементного поля по умолчанию и имя приложения.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "habits"
