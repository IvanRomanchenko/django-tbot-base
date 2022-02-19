from django.apps import AppConfig


class TbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tbot_base'
    verbose_name = 'Настройки Telegram бота'
    verbose_name_plural = 'Настройки Telegram ботов'
