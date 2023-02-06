import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from config.config import Config, load_config 

from handlers.user_handlers import register_user_handlers

config: Config = load_config()


bot: Bot = Bot(token=config.bot.token)

dp: Dispatcher = Dispatcher(bot=bot)

async def set_main_menu(dp: Dispatcher):
    # Создаем список с командами для кнопки menu
    main_menu_commands = [
        types.BotCommand(command='/help', description='Справка по работе бота'),
        types.BotCommand(command='/materials', description='Материалы с занятий')
    ]
    await dp.bot.set_my_commands(main_menu_commands)
if __name__ == "__main__":
    register_user_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)