from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

register = InlineKeyboardButton(text="подать заявку", callback_data="register")
cancel = InlineKeyboardButton(text="отменить заявку", callback_data="cancel")

kb_register = InlineKeyboardMarkup(inline_keyboard=[[register]])
kb_cancel = InlineKeyboardMarkup(inline_keyboard=[[cancel]])

accept = InlineKeyboardButton(text="accept", callback_data="accept_user")
decline = InlineKeyboardButton(text="decline", callback_data="decline_user")

kb_accept = InlineKeyboardMarkup(inline_keyboard=[[accept], [decline]])
