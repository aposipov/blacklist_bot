from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db.db_users import get_icode
from keyboards.user_menu import kb_menu
from keyboards.kb_register import kb_reg_start
from utils.checking import checking_accept
from utils.msg_to_admin import send_from_support, file_was_sent

router = Router()


class FromMenu(StatesGroup):
	fill_text = State()


@router.message(Command(commands='menu'))
async def cmd_menu(message: Message) -> None:
	if checking_accept(message.from_user.id):
		await message.answer(text="Выберите нужный пункт меню:",
		                     reply_markup=kb_menu)
	else:
		await message.answer(text="Вы не прошли регистрацию нажмите "
		                          "\"зарегестрироваться\"!",
		                     reply_markup=kb_reg_start)


@router.message(Command(commands='help'))
async def cmd_help(message: Message) -> None:
	await message.answer(text="Здесь будет описание команд!")


@router.message(Command(commands='support'))
async def cmd_support(message: Message, state: FSMContext) -> None:
	await message.answer(text="Напишите ваш вопрос или предложение!")
	# button cancel
	await state.set_state(FromMenu.fill_text)


@router.message(FromMenu.fill_text)
async def fsm_support(message: Message, state: FSMContext):
	text = message.text
	# check exist
	await send_from_support(message)
	await message.answer(text="Спасибо за ваше обращение!")
	await state.clear()


@router.message(Command(commands='status'))
async def cmd_status(message: Message) -> None:
	await message.answer(text="Бот доступен для запросов!")


@router.message(F.document)
async def cmd_doc(message: Message) -> None:
	from main import bot
	# send adm msg about file
	document = message.document
	ext = document.file_name.split(sep='.')
	path_to_data = f"data/files/{str(message.from_user.id)}.{ext[1]}"
	await bot.download(document, path_to_data)
	await message.answer(text=f"Ваш файл {document.file_name} получен!")
	await file_was_sent(message)


@router.callback_query(F.data == "icode")
async def search_driver(callback: CallbackQuery):
	code = get_icode(callback.from_user.id)
	await callback.message.answer(text="Ниже указанный код вы можете отправить "
	                                   "пользователю для добавления при регистрации!")
	await callback.message.answer(code)
