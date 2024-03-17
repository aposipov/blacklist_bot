from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, PhotoSize
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.user_menu import kb_blacklist
from db.db_drivers import add_driver_bl
from utils.files import get_img

router = Router()


class ProfileBL(StatesGroup):
	fill_fullname = State()
	fill_bd = State()
	fill_driver_id = State()
	fill_img = State()
	fill_comment = State()
	fill_phone = State()
	fill_finish = State()


@router.callback_query(F.data == "add_blacklist")
async def add_blacklist(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer(text="Добавление в черный список. Введите полное ФИО водителя:")
	await state.set_state(ProfileBL.fill_fullname)


@router.message(ProfileBL.fill_fullname)
async def fsm_fullname_bl(message: Message, state: FSMContext):
	# check
	await state.update_data(fullname=message.text)
	await message.answer(text="Введите дату рождения")
	await state.set_state(ProfileBL.fill_bd)


@router.message(ProfileBL.fill_bd)
async def fsm_bd_bl(message: Message, state: FSMContext):
	# check
	await state.update_data(bd=message.text)
	await message.answer(text="Введите номер водительского удостоверения:")
	await state.set_state(ProfileBL.fill_driver_id)


@router.message(ProfileBL.fill_driver_id)
async def fsm_driverid_bl(message: Message, state: FSMContext):
	# check
	await state.update_data(driverid=message.text)
	await message.answer(text="Введите номер телефона водителя с которого "
	                          "он с вами связывался!")
	await state.set_state(ProfileBL.fill_phone)


@router.message(ProfileBL.fill_phone)
async def fsm_phone_bl(message: Message, state: FSMContext):
	await state.update_data(phone=message.text)
	await message.answer(text="Добавьте фото водительского удостоверения, "
	                          "разворот с фотографией водителя! "
	                          "В горизонтальной ориентации!")
	await state.set_state(ProfileBL.fill_img)


@router.message(ProfileBL.fill_img, F.document)
async def fsm_img_bl(message: Message, state: FSMContext):
	text = await state.get_data()
	await state.update_data(img=await get_img(message, text['driverid']))
	await message.answer(text="Введите причину добавления в черный список.")
	await state.set_state(ProfileBL.fill_comment)


@router.message(ProfileBL.fill_comment)
async def fsm_comment_bl(message: Message, state: FSMContext):
	# check
	await state.update_data(comment=message.text)
	text = await state.get_data()
	await message.answer(text="Проверьте, что вы ввели верные данные!")
	await message.answer(
		text="Будет добавлен в черный спискок! \n"
		     + text['fullname'] + "\n"
		     + text['bd'] + "\n"
		     + text['driverid'] + "\n"
		     + "\n"
		     + text['comment'],
		reply_markup=kb_blacklist)
	await state.set_state(ProfileBL.fill_finish)


@router.callback_query(F.data == "apply_bl")
async def apply(callback: CallbackQuery, state: FSMContext):
	profile = await state.get_data()
	tg_id = callback.from_user.id
	add_driver_bl(profile, tg_id)
	await callback.message.answer(text="Водитель добавлен в черный список!")
	await state.clear()


# @router.message(ProfileBL.fill_finish, F.data == "apply_bl")
# async def apply(message: Message, state: FSMContext):
# 	profile = await state.get_data()
# 	tg_id = message.from_user.id
# 	add_driver_bl(profile, tg_id)
# 	await message.answer(text="Водитель добавлен в черный список!")
# 	await state.clear()
