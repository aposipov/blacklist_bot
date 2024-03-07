from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

search = InlineKeyboardButton(text="поиск водителя", callback_data="search_user")
add = InlineKeyboardButton(text="добавить в черный список", callback_data="add_user")

kb_menu = InlineKeyboardMarkup(inline_keyboard=[[search], [add]])
