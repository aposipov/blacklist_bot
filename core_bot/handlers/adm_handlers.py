from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db.db_adm import accept_user

router = Router()


class Form(StatesGroup):
	fill_user_id = State()


@router.callback_query(F.data == "accept_user")
async def accept(callback: CallbackQuery, state: FSMContext):
	await callback.message.answer("input user_id!")
	await state.set_state(Form.fill_user_id)


@router.message(Form.fill_user_id)
async def fsm_user_id(message: Message, state: FSMContext):
	accept_user(int(message.text))
	await message.answer(message.text + " is accept!")
	await state.clear()


@router.message(Command(commands='adm'))
async def cmd_help(message: Message) -> None:
	await message.answer(text="/adm - show all cmds\n"
	                          "/getid - show user_id and chat_id\n"
	                          "/accept - accept User\n")


@router.message(Command(commands='getid'))
async def cmd_help(message: Message) -> None:
	await message.answer(text="ID: " + str(message.from_user.id) + "\n"
	                        "CHAT ID: " + str(message.chat.id) + "\n")


@router.message(Command(commands='accept'))
async def cmd_help(message: Message, command: CommandObject) -> None:
	userid = command.args
	accept_user(int(userid))
	await message.answer(text=userid + " is accept!")
