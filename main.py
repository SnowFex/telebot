from aiogram import Bot, Dispatcher, F
import asyncio
import os
from dotenv import load_dotenv
from utils.commands import set_command
from handlers.start import get_start
from aiogram.filters import Command
from aiogram.types import Message
from handlers.info import get_info
from handlers.linkboard import inline
from handlers.register import start_register, register_name, register_city
from state.registr import RegisterState
from handlers.Json import get_weather
import requests

load_dotenv()

token = os.getenv('TOKEN')


bot = Bot(token=token)
dp = Dispatcher()

async def start():
    await set_command(bot)


async def startline():
    await inline(bot)

dp.message.register(get_start, Command(commands='start'))
dp.message.register(get_info, Command(commands='info'))


# Регистрация пользователя
dp.message.register(start_register, F.text =='хочу получать рассылку')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_city, RegisterState.regcity)


if __name__ == '__main__':
    dp.run_polling(bot)