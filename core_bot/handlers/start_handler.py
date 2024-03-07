from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards.register import kb_register, kb_cancel

from utils.msg_to_admin import send_adm

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Report(StatesGroup):
    fill_report = State()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    # add_to_file(message)
    # add_to_db(message)
    await message.answer(text=
                         "Доброго времени суток!\n"
                         "Нажмите кнопку \"подать заявку\" для продолжения",
                         reply_markup=kb_register)


@router.callback_query(F.data == "register")
async def register(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Report.fill_report)
    await callback.message.answer("Напишите, как давно вы занимаетесь арендой?"
                                  "\nС кем из арендодателей знакомы?"
                                  "\nЕсли передумали можете ничего не отвечать"
                                  " или нажать кнопку \"отменить заявку\"",
                                  reply_markup=kb_cancel)


@router.message(Report.fill_report)
async def fsm_report(message: Message, state: FSMContext) -> None:
    report = message.text
    user = message.from_user.id
    name = message.from_user.username
    await send_adm(report, str(user), name)
    await message.answer("Благодарим за ваше обращение!")
    await state.clear()
