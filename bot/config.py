"""Загрузка конфигурации из переменных окружения (.env)."""

import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
WORK_CHAT_ID = os.getenv("WORK_CHAT_ID", "")
CALENDAR_ID = os.getenv("CALENDAR_ID", "")
TIMEZONE = os.getenv("TIMEZONE", "Europe/Moscow")
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON", "credentials.json")


def validate_config() -> None:
    """Проверяет наличие обязательных переменных. Бросает RuntimeError при ошибке."""
    missing = []
    if not BOT_TOKEN:
        missing.append("BOT_TOKEN")
    if not WORK_CHAT_ID:
        missing.append("WORK_CHAT_ID")
    if missing:
        raise RuntimeError(
            "Не заданы обязательные переменные окружения: "
            + ", ".join(missing)
            + ". Заполните файл .env (см. .env.example)."
        )

    if not CALENDAR_ID:
        logger.warning(
            "CALENDAR_ID не задан — события в Google Calendar создаваться не будут."
        )
    elif not os.path.exists(GOOGLE_CREDENTIALS_JSON):
        logger.warning(
            "Файл учётных данных Google '%s' не найден — "
            "события в Google Calendar создаваться не будут.",
            GOOGLE_CREDENTIALS_JSON,
        )
