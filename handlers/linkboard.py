from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline = InlineKeyboardButton(text='самая красивая девушка', url='https://vk.com/chris_hr')

keyboarde = InlineKeyboardMarkup(inline_keyboard=[[inline]], resize_keyboard=True, one_time_keyboard=True)