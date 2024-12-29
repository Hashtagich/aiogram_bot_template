from aiogram import Bot
from aiogram.types import BotCommand, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_COMMANDS, LEXICON, LEXICON_COMMANDS_ADMIN
from filters.filters import IsAdmin


async def set_main_menu(bot: Bot):
    """Функция для настройки кнопки Menu бота."""

    if IsAdmin:
        db = LEXICON_COMMANDS_ADMIN
    else:
        db = LEXICON_COMMANDS

    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command,
        description in db.items()
    ]
    await bot.set_my_commands(main_menu_commands)



