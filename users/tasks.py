from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def deactivate_inactive_users():
    """
    Деактивирует пользователей, которые не входили в систему в течение последнего месяца.

    """
    one_month_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    inactive_users.update(is_active=False)