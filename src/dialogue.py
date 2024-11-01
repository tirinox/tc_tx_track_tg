from aiogram import Bot, Dispatcher, types, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart


class TransactionBot:
    def __init__(self, token):
        self.bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()

        # Register handlers
        self.dp.message.register(self.start_command, CommandStart())
        self.dp.message.register(self.add_command, Command('add'))

    async def start_command(self, message: types.Message):
        # Handler for /start command
        # Extract parameters if any
        try:
            tx_id = message.text.split(' ')[1].strip()
        except IndexError:
            tx_id = ''

        if tx_id:
            await message.reply(f"Received TX ID: {tx_id}")
        else:
            await message.reply("Welcome to the Transaction Tracking Bot!")

    async def add_command(self, message: types.Message):
        # Handler for /add command
        await message.reply("Please send the TX ID you want to add.")

    async def run(self):
        # And the run events dispatching
        await self.dp.start_polling(self.bot)
