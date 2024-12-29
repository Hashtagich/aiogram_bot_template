from aiogram.types import Message
from aiogram.filters import BaseFilter
from lexicon.lexicon import LEXICON_COMMANDS
from database.database import get_admin_ids


class IsMenuCommand(BaseFilter):
    """Фильтр для проверки, что передана команда или текст для активации отображения главного меню."""

    async def __call__(self, message: Message) -> bool:
        return message.text == '/menu' or message.text.capitalize() == LEXICON_COMMANDS['/menu']


class IsAdmin(BaseFilter):
    """Фильтр для проверки, что пользователь является админом."""

    def __init__(self, admin_ids: tuple[int] = get_admin_ids()) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids
