from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db.db_adm import accept_user, decline_user
from utils.msgs import msg, shout

router = Router()


class FormAdm(StatesGroup):
	fill_user_id = State()


class UserMsg(StatesGroup):
	fill_msg = State()
	fill_forall = State()


@router.callback_query(F.data == "accept_user")
async def accept(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer("input user_id!")
	await state.set_state(FormAdm.fill_user_id)


@router.message(FormAdm.fill_user_id)
async def fsm_user_id(message: Message, state: FSMContext):
	from main import bot
	accept_user(int(message.text))
	await message.answer(message.text + " is accept!")
	await bot.send_message(chat_id=int(message.text), text="Ваша регситрация одобрена! "
	                        "Чтобы ознакомиться с возможностями нажмите /menu")
	await state.clear()


@router.message(Command(commands='adm'))
async def cmd_adm(message: Message) -> None:
	#check ADMIN ID
	await message.answer(text="/adm - show all cmds\n"
	                          "/msg - msg for user\n"
	                          "/shout - msg for all\n"
	                          "/getid - show user_id and chat_id\n"
	                          "/get_phone - get user phone number\n"
	                          "/accept - accept User\n"
	                          "/decline - no add\n")


@router.message(Command(commands='getid'))
async def cmd_getid(message: Message) -> None:
	await message.answer(text="ID: " + str(message.from_user.id) + "\n"
	                        "CHAT ID: " + str(message.chat.id) + "\n"
	                        "THREAD_ID: " + str(message.message_thread_id))


@router.message(Command(commands='msg'))
async def cmd_msg(message: Message, command: CommandObject, state: FSMContext) -> None:
	# check adm
	await state.update_data(userid=command.args)
	await message.answer(text="Input text ...")
	await state.set_state(UserMsg.fill_msg)


@router.message(UserMsg.fill_msg)
async def fsm_msg(message: Message, state: FSMContext):
	text = message.text
	data = await state.get_data()
	userid = data.get('userid')
	await msg(userid, text)
	await message.answer("✅ msg was sended!")
	await state.clear()


@router.message(Command(commands='shout'))
async def cmd_shout(message: Message, state: FSMContext) -> None:
	# check adm
	await message.answer(text="Input text ...")
	await state.set_state(UserMsg.fill_forall)


@router.message(UserMsg.fill_forall)
async def fsm_shout(message: Message, state: FSMContext):
	await shout(message.text)
	await message.answer("✅ msg was sended!")
	await state.clear()


@router.message(Command(commands='accept'))
async def cmd_accept(message: Message, command: CommandObject) -> None:
	from main import bot
	userid = command.args
	accept_user(int(userid))
	await message.answer(text=userid + " accepted!")
	await bot.send_message(chat_id=int(userid),
	                       text="Ваша регситрация одобрена! "
	                    "Чтобы ознакомиться с возможностями нажмите /menu")


@router.message(Command(commands='decline'))
async def cmd_accept(message: Message, command: CommandObject) -> None:
	from main import bot
	userid = command.args
	decline_user(int(userid))
	await message.answer(text=userid + " rejected!")
	await bot.send_message(chat_id=int(userid),
	                       text="Ваша регистрация отменена!")
