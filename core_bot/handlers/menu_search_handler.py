from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from keyboards.user_menu import kb_menu, kb_search
from db.db_drivers import add_driver_db, search_driver_db
from utils.checking import checking_accept

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Profile(StatesGroup):
	fill_fullname = State()
	fill_bd = State()
	fill_id_driver = State()


# @router.message(Command(commands='menu'))
# async def cmd_menu(message: Message) -> None:
# 	if checking_accept(message.from_user.id):
# 		await message.answer(text="Выберите нужный пункт меню:", reply_markup=kb_menu)
# 	else:
# 		await message.answer(text="Вы не прошли регистрацию нажмите /start")


@router.callback_query(F.data == "search_driver")
async def search_driver(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer(text="Введите полное ФИО водителя:")
	await state.set_state(Profile.fill_fullname)


@router.message(Profile.fill_fullname)
async def fsm_fullname(message: Message, state: FSMContext) -> None:
	# check fullname func empty, correct
	await state.update_data(name=message.text)
	await message.answer(text="Введите дату рождения")
	await state.set_state(Profile.fill_bd)


@router.message(Profile.fill_bd)
async def fsm_bd(message: Message, state: FSMContext):
	# check bd correct
	await state.update_data(bd_driver=message.text)
	await message.answer(text="Введите номер ВУ:")
	await state.set_state(Profile.fill_id_driver)


@router.message(Profile.fill_id_driver)
async def fsm_id_driver(message: Message, state: FSMContext):
	await state.update_data(id_driver=message.text)
	text = await state.get_data()
	await message.answer(text="Проверьте, что вы ввели верные данные!")
	await message.answer(text=text['name'] + "\n" + text['bd_driver'] + "\n" + text['id_driver'],
	                     reply_markup=kb_search)


@router.callback_query(F.data == "edit_fname")
async def edit_fname(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer(text="Введите полное ФИО водителя:")
	await state.set_state(Profile.fill_fullname)


@router.callback_query(F.data == "edit_bd")
async def edit_bd(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer(text="Введите дату рождения:")
	await state.set_state(Profile.fill_bd)


@router.callback_query(F.data == "edit_id")
async def edit_driver_id(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer(text="Введите номер ВУ:")
	await state.set_state(Profile.fill_id_driver)


@router.callback_query(F.data == "apply")
async def apply(callback: CallbackQuery, state: FSMContext):
	profile = await state.get_data()
	tg_id = callback.from_user.id
	add_driver_db(profile, tg_id)
	result = search_driver_db(profile)
	if result:
		for line in result:
			await callback.message.answer(text="В черном списке:\n"
			                    + line[0]
			                    + " " + line[3]
			                    + " " + line[4]
			                    + " " + line[5] + "\n")
		await state.clear()
	else:
		await callback.message.answer(text="В черном списке водитель не найден!")
	await state.clear()

# @router.callback_query(F.data == "add_blacklist")
# async def register(callback: CallbackQuery):
# 	await callback.message.answer(text="You press ADD Blacklist")
