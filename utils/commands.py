from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat


async def set_command(bot: Bot, chat_id: int):
    commands = [BotCommand(command='start', description='старт'), BotCommand(command='info', description='инфо')]
    await bot.set_my_commands(commands, BotCommandScopeChat(chat_id=chat_id))
