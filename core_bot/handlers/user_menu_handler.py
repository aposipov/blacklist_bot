from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.user_menu import kb_menu

router = Router()


@router.message(Command(commands='menu'))
async def cmd_help(message: Message) -> None:
	await message.answer(text="Выберите нужный пункт меню:", reply_markup=kb_menu)

