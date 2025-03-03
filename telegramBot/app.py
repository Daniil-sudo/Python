import asyncio
import os
from email import message_from_bytes
from aiogram import Bot, Dispatcher, types
from  aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats
from pyexpat.errors import messages

import aiofiles

#все подключаемое переменных окружения до дополнительных файлов в окружении
from dotenv import find_dotenv,load_dotenv

from handlers.user_privat import upr
from common.bot_cmd_list import private


load_dotenv(find_dotenv())

bot=Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp=Dispatcher()
dp.include_router(upr)
#DATA_FILE = ("user_responses.json")

async def main():
    await bot.delete_webhook(drop_pending_updates=True) #команда, что бы бот не отвечал на вопросы, когда был выключен
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private,scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot,allowed_updates=["message","edited_message"])

asyncio.run(main())

#bot = Bot('7889721307:AAG2y9cltrZdkG4mzcZdqo1b6OvF8S126sE')
