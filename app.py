import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
from dotenv import load_dotenv, find_dotenv

from middleweares.db import DataBaseSession

load_dotenv(find_dotenv())

from common.bot_command_list import private
from database.engine import create_db, drop_db, session_maker
from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from handlers.admin_private import admin_router

# from middleweares.db import CounterMiddleware


ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []
dp = Dispatcher()
dp.include_routers(user_private_router, user_group_router, admin_router)


async def on_startup(bot):
   # await drop_db() # Закоментить после 1го запуска
    await create_db()


async def on_shutdown(bot):
    print('Бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await create_db()
    await bot.delete_webhook(drop_pending_updates=True)
    #await bot.set_my_commands(commands=private,
                              #scope=types.BotCommandScopeAllPrivateChats())
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats()) # Закоментить после первого запуска
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
