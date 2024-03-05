from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardMarkup

router = Router()

contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)

kb2 = ReplyKeyboardMarkup(keyboard=[[contact_btn], [geo_btn]])


def get_kb():
    buttons = [
        [InlineKeyboardButton(text='first button', callback_data='1')],
        [InlineKeyboardButton(text='second button', callback_data='2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    # add_to_file(message)
    # add_to_db(message)
    await message.answer(text=
                         "Доброго времени суток!\n"
                         "Если будут вопросы наберите /help", reply_markup=kb2)

