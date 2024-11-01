import asyncio
import logging
import os

from aiogram import Bot
from dotenv import load_dotenv

from dialogue import TransactionBot
from logs import setup_logs, WithLogger

# load .env
load_dotenv()


class App(WithLogger):
    def __init__(self):
        log_level = logging.INFO
        setup_logs(log_level, colorful=True)
        super().__init__()

    async def run(self):
        self.logger.info('Starting the bot...')
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not bot_token:
            raise ValueError('TELEGRAM_BOT_TOKEN is not set')

        bot = TransactionBot(bot_token)
        await bot.run()


if __name__ == '__main__':
    app = App()
    asyncio.run(app.run())
