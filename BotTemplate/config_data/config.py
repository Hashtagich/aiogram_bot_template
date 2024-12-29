from dataclasses import dataclass
import os
from environs import Env
from typing import List


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    # user_ids: List[str]
    # admin_ids: List[str]
    # dev_ids: List[str]


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
        )
        # user_ids=os.getenv("USER_IDS").split(' '),
        # admin_ids=os.getenv("ADMIN_IDS").split(' '),
        # dev_ids=os.getenv("DEV_IDS").split(' ')
    )
