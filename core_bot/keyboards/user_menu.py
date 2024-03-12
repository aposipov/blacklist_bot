from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inv_code = InlineKeyboardButton(text="код для приглашения", callback_data="icode")
search = InlineKeyboardButton(text="поиск водителя", callback_data="search_driver")
add = InlineKeyboardButton(text="добавить в черный список", callback_data="add_blacklist")
tracking = InlineKeyboardButton(text="❌ отслеживать", callback_data="tracking")

kb_menu = InlineKeyboardMarkup(inline_keyboard=[[inv_code], [search], [add], [tracking]])

apply = InlineKeyboardButton(text="✅ данные верны", callback_data="apply")
edit_fullname = InlineKeyboardButton(text="✏️ изменить ФИО", callback_data="edit_fname")
edit_bd = InlineKeyboardButton(text="✏️ изменить Дату Рождения", callback_data="edit_bd")
edit_id = InlineKeyboardButton(text="✏️ изменить Номер ВУ", callback_data="edit_id")

kb_search = InlineKeyboardMarkup(inline_keyboard=[[apply], [edit_fullname],
                                                  [edit_bd], [edit_id]])
