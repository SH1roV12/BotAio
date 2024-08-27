from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import types


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Узнать погоду🌤️")]
], resize_keyboard=True,
    input_field_placeholder="Выберите из меню")