from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from keyboards.user_menu import kb_menu, kb_search

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class ProfileBL(StatesGroup):
	fill_fullname = State()
	fill_bd = State()
	fill_driver_id = State()
	fill_img = State()
	fill_comment = State()


@router.callback_query(F.data == "add_blacklist")
async def add_blacklist(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer(text="BL Введите полное ФИО водителя:")
	await state.set_state(ProfileBL.fill_fullname)


@router.message(ProfileBL.fill_fullname)
async def fsm_fullname(message: Message, state: FSMContext):
	await state.update_data(fullname=message.text)
	await message.answer(text="BL Введите дату рождения")
	await state.set_state(ProfileBL.fill_bd)
	await state.clear()

