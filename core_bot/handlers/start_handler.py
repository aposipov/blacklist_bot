from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards.kb_register import kb_reg_start, kb_cancel_start, kb_invite

from utils.msg_to_admin import send_adm
from db.db_users import add_user_db, add_phone, add_about_user, add_icode

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class FormStart(StatesGroup):
    fill_phone = State()
    fill_request = State()
    fill_code = State()
    fill_trash = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    add_user_db(message)
    await message.answer(text=f"Доброго времени суток, {message.from_user.first_name}!\n"
                              "Введите ваш номер телефона в формате \"89991231234\"")
    await state.set_state(FormStart.fill_phone)


@router.message(FormStart.fill_phone)
async def fsm_phone(message: Message, state: FSMContext):
    phone = message.text
    userid = message.from_user.id
    # await state.update_data(phone=phone)
    #check empty and valid
    add_phone(phone, userid)
    await message.answer(text=
                             "Чтобы использовать возможности Бота "
                             "пройдите процесс регистрации! \n"
                             "Нажмите кнопку \"зарегестрироваться\"",
                             reply_markup=kb_reg_start)
    await state.set_state(FormStart.fill_trash)


@router.callback_query(F.data == "reg_start")
async def register_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Напишите, как давно вы занимаетесь арендой?"
                        "\nС кем из арендодателей знакомы?"
                        "\nЕсли передумали можете ничего не отвечать"
                        " или нажать кнопку \"отменить регистрацию\"",
                        reply_markup=kb_cancel_start)
    await state.set_state(FormStart.fill_request)


@router.message(FormStart.fill_request)
async def fsm_report(message: Message, state: FSMContext) -> None:
    #check empty
    about = message.text
    userid = message.from_user.id
    add_about_user(about, userid)
    # uname = message.from_user.username
    await state.update_data(about=about)
    # await send_adm(about, str(userid), uname)
    await message.answer("Если у Вас есть персональный \"код приглашения\" "
                         "от одного из пользователей Бота "
                         "рекомендуем его добавить. Это сильно повлияет на "
                         "срок рассмотрения и одобрение заявки!",
                         reply_markup=kb_invite)
    await state.set_state(FormStart.fill_trash)


@router.callback_query(F.data == "invite_code")
async def reg_invite(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите \"код приглашения\"!")
    await state.set_state(FormStart.fill_code)


@router.message(FormStart.fill_code)
async def fsm_code(message: Message, state: FSMContext) -> None:
    code = message.text
    uname = message.from_user.username
    fullname = message.from_user.full_name
    #check exist code
    userid = message.from_user.id
    add_icode(code, userid)
    storage = await state.get_data()
    await send_adm(storage['about'], str(userid), uname, fullname, code)
    await message.answer(f"{message.from_user.first_name}, спасибо! "
                                  "Заявка будет рассмотрена в течении суток!")
    await state.clear()


@router.callback_query(F.data == "no_code")
async def reg_no_code(callback: CallbackQuery, state: FSMContext):
    uname = callback.from_user.username
    fullname = callback.from_user.full_name
    userid = callback.from_user.id
    storage = await state.get_data()
    await send_adm(storage['about'], str(userid), uname, fullname, 'no code')
    await callback.message.answer(f"{callback.message.from_user.first_name}, спасибо! "
                                  "Рассмотрение заявки займет до 3х суток!")
    await state.clear()


@router.callback_query(F.data == "cancel")
async def reg_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Если захотите продожить регистрацию, нажмите кнопку!",
                                  reply_markup=kb_reg_start)
    await state.clear()
