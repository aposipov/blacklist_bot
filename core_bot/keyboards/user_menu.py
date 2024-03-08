from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

search = InlineKeyboardButton(text="поиск водителя", callback_data="search_driver")
add = InlineKeyboardButton(text="добавить в черный список", callback_data="add_blacklist")

kb_menu = InlineKeyboardMarkup(inline_keyboard=[[search], [add]])

apply = InlineKeyboardButton(text="apply", callback_data="apply")
edit_fullname = InlineKeyboardButton(text="edit full name", callback_data="edit_fname")
edit_bd = InlineKeyboardButton(text="edit bd", callback_data="edit_bd")
edit_id = InlineKeyboardButton(text="edit id driver", callback_data="edit_id")

kb_search = InlineKeyboardMarkup(inline_keyboard=[[apply], [edit_fullname],
                                                  [edit_bd], [edit_id]])
