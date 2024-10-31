import asyncio
import os

from aiogram import Bot
from dotenv import load_dotenv

# load .env
load_dotenv()


class App:
    async def run(self):
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not bot_token:
            raise ValueError('TELEGRAM_BOT_TOKEN is not set')

        bot = Bot(bot_token)
        await bot.send_message(chat_id=os.getenv('TELEGRAM_CHAT_ID'), text='Hello, world!')


if __name__ == '__main__':
    app = App()
    asyncio.run(app.run())
