from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db.db_users import get_icode

router = Router()


@router.callback_query(F.data == "icode")
async def search_driver(callback: CallbackQuery):
	code = get_icode(callback.from_user.id)
	await callback.message.answer(text="Ниже указанный код вы можете отправить "
	                                   "пользователю для добавления!")
	await callback.message.answer(code)
