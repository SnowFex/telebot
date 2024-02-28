from aiogram import Bot
from aiogram.types import Message
from keyboards.link import keyboards


async def get_info(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text='Я бот, который будет отправлять тебе рассылку о погоде каждый день\n'
                                                      , reply_markup=keyboards)