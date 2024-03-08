from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards.register import kb_register, kb_cancel

from utils.msg_to_admin import send_adm
from db.db_users import add_user_db, add_about_user, add_phone

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Form(StatesGroup):
    fill_phone = State()
    fill_request = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    add_user_db(message)
    await message.answer(text="Доброго времени суток!\n"
                              "Введите ваш номер телефона в формате +79991111111")
    await state.set_state(Form.fill_phone)


# @router.message(CommandStart())
# async def cmd_start(message: Message) -> None:
#     add_user_db(message)
#     await message.answer(text=
#                          "Доброго времени суток!\n"
#                          "Нажмите кнопку \"подать заявку\" для продолжения",
#                          reply_markup=kb_register)


@router.message(Form.fill_phone)
async def fsm_phone(message: Message, state: FSMContext):
    phone = message.text
    user = message.from_user.id
    #check empty and valid
    add_phone(phone, user)
    await message.answer("Напишите, как давно вы занимаетесь арендой?"
                                  "\nС кем из арендодателей знакомы?"
                                  "\nЕсли передумали можете ничего не отвечать"
                                  " или нажать кнопку \"отменить заявку\"",
                                  reply_markup=kb_cancel)
    await state.set_state(Form.fill_request)


@router.callback_query(F.data == "register")
async def register(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Form.fill_request)
    await callback.message.answer("Напишите, как давно вы занимаетесь арендой?"
                                  "\nС кем из арендодателей знакомы?"
                                  "\nЕсли передумали можете ничего не отвечать"
                                  " или нажать кнопку \"отменить заявку\"",
                                  reply_markup=kb_cancel)


@router.message(Form.fill_request)
async def fsm_report(message: Message, state: FSMContext) -> None:
    #check empty
    report = message.text
    userid = message.from_user.id
    add_about_user(report, userid)
    name = message.from_user.username
    await send_adm(report, str(userid), name)
    await message.answer("Благодарим за ваше обращение!")
    await state.clear()
