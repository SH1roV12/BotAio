from aiogram.fsm.state import State, StatesGroup

class GetWeather(StatesGroup):
    city = State()