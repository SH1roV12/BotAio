import asyncio
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher

import requests
from app.handlers import router

load_dotenv()


bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)



asyncio.run(main()) 