from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ras = KeyboardButton(text='хочу получать рассылку')

keyboards = ReplyKeyboardMarkup(keyboard=[[ras]], resize_keyboard=True, one_time_keyboard=True)
