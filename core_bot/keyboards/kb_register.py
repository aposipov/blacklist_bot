from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

register = InlineKeyboardButton(text="зарегестрироваться", callback_data="reg_start")
kb_reg_start = InlineKeyboardMarkup(inline_keyboard=[[register]])

cancel = InlineKeyboardButton(text="отменить регистрацию", callback_data="cancel")
kb_cancel_start = InlineKeyboardMarkup(inline_keyboard=[[cancel]])

invite = InlineKeyboardButton(text="код приглашения", callback_data="invite_code")
no_code = InlineKeyboardButton(text="код отсутствует", callback_data="no_code")
kb_invite = InlineKeyboardMarkup(inline_keyboard=[[invite], [no_code]])

accept = InlineKeyboardButton(text="accept", callback_data="accept_user")
decline = InlineKeyboardButton(text="decline", callback_data="decline_user")
kb_accept = InlineKeyboardMarkup(inline_keyboard=[[accept], [decline]])
