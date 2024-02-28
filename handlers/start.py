from aiogram import Bot
from aiogram.types import Message
from keyboards.link import keyboards
from handlers.linkboard import keyboarde
from utils.commands import set_command
async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text='Привет, Пользователь!', reply_markup=keyboarde)
    await set_command(bot, chat_id=message.chat.id)