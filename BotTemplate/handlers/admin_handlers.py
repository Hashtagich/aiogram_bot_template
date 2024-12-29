from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from filters.filters import IsAdmin, IsMenuCommand
from lexicon.lexicon import LEXICON

admin_handlers_router = Router()

admin_handlers_router.message.filter(IsAdmin())


@admin_handlers_router.message(Command(commands='allert'))
async def process_main_menu_command(message: Message):
    """Хэндлер срабатывает на команду /allert"""
    await message.answer(text='текст allert')


