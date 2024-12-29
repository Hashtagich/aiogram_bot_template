import asyncio
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON

# from copy import deepcopy
# from database.database import load_json_data, save_json_data, user_dict_template

user_handlers_router = Router()


@user_handlers_router.message(CommandStart())
async def process_start_command(message: Message):
    """Хэндлер срабатывает на команду /start"""

    await message.answer(text=LEXICON['/start'])

    # db = load_json_data()
    # if str(message.from_user.id) not in db.keys():
    #     db[message.from_user.id] = deepcopy(user_dict_template)
    #     db[message.from_user.id]['user_name'] = message.from_user.username
    #
    # save_json_data(data=db)


@user_handlers_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """Хэндлер срабатывает на команду /help"""
    await message.answer(text=LEXICON['/help'])


