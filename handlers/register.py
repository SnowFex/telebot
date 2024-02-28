import os

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from mysql.connector import cursor

from state.registr import RegisterState
from database.dbmysql import connection
import mysql.connector
import requests
from database.config import OPEN_WEATHER_TOKEN


async def start_register(message: Message, state: FSMContext):

    await message.answer(f'Давайте начнём регистрацию!\n'
                         f'Как вас зовут?')
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Приятно познакомится, {message.text}!\n'
                         f'Укажите город в котором вы живёте?')
    await state.update_data(regName=message.text)
    await state.set_state(RegisterState.regcity)

async def register_city(message: Message, state: FSMContext):
    await state.update_data(regcity=message.text)
    user_id = message.from_user.id
    reg_data = await state.get_data()
    reg_name = reg_data.get('regName')
    reg_city = reg_data.get('regcity')
    msg = f'Приятно познакомтся {reg_name}!\n' \
          f'Ваш город - {reg_city}.'

    try:
        mycursor = connection.cursor()
        sql = """INSERT INTO weaher (id, name, city) VALUES (%s, %s, %s)"""
        val = [user_id, reg_name, reg_city]
        mycursor.execute(sql, val)
        connection.commit()
    except mysql.connector.Error as error:
        print(error)

    def select_user_id(self, user_id):
        users = self.cursor.execute("""SELECT * FROM weaher WHERE id = %s""", (user_id))
        return users.fetchone()

    #await message.answer(msg)

    def get_weather(reg_city, OPEN_WEATHER_TOKEN):
        # try:
        url = f" http://api.weatherapi.com/v1/current.json?key={OPEN_WEATHER_TOKEN}&q={reg_city}"

        response = requests.get(url)

        # print("status", response.status_code)
        # print("r", response)
        data = response.json()
        # print(data)
        city = data['location']['name']
        cur_weather = data['current']['temp_c']
        humidity = data['current']['humidity']

        weather_message = (f'Погода в городе {reg_city}\n'
                           f'Температура: {cur_weather}\n'
                           f'Влажность:  {humidity} %')

        return weather_message

    # except Exception as e:
    #  print(e)

    result = get_weather(reg_city=reg_city, OPEN_WEATHER_TOKEN=OPEN_WEATHER_TOKEN)
    await message.answer(result)
    await state.clear()