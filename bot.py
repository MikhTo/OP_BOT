import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config.config import Config, load_config 


config: Config = load_config()


bot: Bot = Bot(token=config.bot.token)

dp: Dispatcher = Dispatcher(bot=bot)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)