from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.user_menu import kb_menu

router = Router()


@router.message(Command(commands='status'))
async def cmd_help(message: Message) -> None:
	await message.answer(text="Бот доступен для запросов!")
