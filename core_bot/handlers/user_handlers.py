from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db.db_users import get_icode
from keyboards.user_menu import kb_menu, kb_search
from keyboards.kb_register import kb_reg_start
from db.db_drivers import add_driver_db
from utils.checking import checking_accept

router = Router()


@router.message(Command(commands='menu'))
async def cmd_menu(message: Message) -> None:
	if checking_accept(message.from_user.id):
		await message.answer(text="Выберите нужный пункт меню:",
		                     reply_markup=kb_menu)
	else:
		await message.answer(text="Вы не прошли регистрацию нажмите "
		                          "\"зарегестрироваться\"!",
		                     reply_markup=kb_reg_start)


@router.callback_query(F.data == "icode")
async def search_driver(callback: CallbackQuery):
	code = get_icode(callback.from_user.id)
	await callback.message.answer(text="Ниже указанный код вы можете отправить "
	                                   "пользователю для добавления при регистрации!")
	await callback.message.answer(code)
