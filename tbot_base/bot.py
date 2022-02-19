from telebot import TeleBot, types
from loguru import logger


class TBot(TeleBot):
    """ Base Telegram bot config """

    def __init__(self):
        try:
            from .models import BotConfig

            self.config = BotConfig.objects.get(is_active=True)
            self.token = self.config.token

        except Exception as e:
            logger.error(e)

            self.token = 'foo'

        super().__init__(self.token, parse_mode='HTML', threaded=False)

    @staticmethod
    def update(json_data):
        return types.Update.de_json(json_data)


tbot = TBot()
