from typing import Union
from environs import Env

class TgBot:
    def __init__(self, token: str, admin_id:int):
        self.token = token
        self.admin_id = admin_id

class Config:
    def __init__(self, bot: TgBot):
        self.bot = bot

def load_config(path: Union[str, None] = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(bot=TgBot(token=env("BOT_TOKEN"), admin_id=env("ADMIN_ID")))