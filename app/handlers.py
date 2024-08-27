import random
from aiogram import Router, Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.types import message
import app.keyboard as kb # type: ignore
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import requests
from app.states import GetWeather



router = Router()






@router.message(CommandStart())
async def start_com(message: types.message):
    await message.reply_animation(animation = "https://media1.tenor.com/m/-NJHCQmv_fwAAAAC/excessive-heat-warning-sunshine.gif", caption = "Привет,это новый  бот для поиска погоды",
                        reply_markup=kb.main)


@router.message(F.photo)
async def photo(message: types.message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")

@router.message(F.sticker)
async def sticker(message: types.message):
    await message.answer(message.sticker.file_id)






@router.message(Command("give"))
async def start_com(message: types.message):
    await message.answer_photo(photo= "https://s0.rbk.ru/v6_top_pics/resized/600xH/media/img/1/18/347128400924181.webp")

    
@router.message(F.text == "Узнать погоду🌤️")
async def weth(message:types.message, state:FSMContext):
    await state.set_state(GetWeather.city)
    await message.answer("Введите ваш город в котором хотите получить погоду")


@router.message(GetWeather.city)
async def weth2(message: types.message, state:FSMContext):
    city = message.text 
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=658467b0637594e3e8cb8360fcd8e8b2'
        weather_data = requests.get(url).json()
        temp = round(weather_data['main']['temp'])
        temp_feels = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        temp -= 275.45
        temp_feels -= 275.45
        await message.answer_animation(animation ='https://media.tenor.com/z5gDoFCYzNQAAAAi/we-support-clean-energy-jobs-climate-action-now.gif',caption = (f"--------------Погода в {city}---------------\n"
                            f"----Температура Воздуха:{round(temp)}----\n"
                            f'\n'
                            f'---Ощущается как: {round(temp_feels)}---\n'
                            f'\n'
                            f'--Скорость ветра: {wind_speed}--'
                            ))
    except KeyError:
          await message.answer('Не найден город')
    await state.clear()
    



@router.message()
async def echo(message: types.message):
    text = message.text.lower()

    if text in ["ку", "привет", "здравствуй"]:
        await message.answer("И тебе привет")
    elif text == "пока":
        await message.reply("покеда") 
    elif text == "дибил":
        await message.answer_sticker(sticker = "CAACAgIAAxkBAAPvZsyLM9Ygm8r_YamGqHhKFPSQxQMAAo9RAAJ50slIAZYhb3_NSJ41BA")
    elif text == "спасибо":
        message.answer("Всегда пожалуйста😊")   
    else:
        await message.answer("Простите,но я вас не понимаю(", reply_markup = kb.main)