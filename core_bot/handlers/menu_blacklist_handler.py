from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from keyboards.user_menu import kb_menu, kb_search

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data == "add_blacklist")
async def register(callback: CallbackQuery):
	await callback.message.answer(text="You press ADD Blacklist")
