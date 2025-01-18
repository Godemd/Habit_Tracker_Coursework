import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)
TOKEN = settings.TELEGRAM_BOT_TOKEN
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


def send_telegram_message(chat_id, message):
    """
    Отправляет сообщение в Telegram через HTTP-запрос к API Telegram Bot.
    Примечание:
        Для работы функции требуется заранее настроенный URL для API Telegram Bot.
    """
    try:
        data = {"chat_id": chat_id, "text": message}
        response = requests.post(URL, data=data)
        response.raise_for_status()
        return True
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения в Telegram: {str(e)}")
        return False
