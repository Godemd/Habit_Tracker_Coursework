from notifications.tasks import send_habit_reminder


# Create your views here.
def perform_update(self, serializer):
    """
    Выполняет обновление объекта и отправляет напоминание о привычке.

    """
    instance = serializer.save()
    send_habit_reminder.delay(self.request.user.id, instance.id)
