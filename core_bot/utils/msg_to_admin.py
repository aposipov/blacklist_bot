from main import bot
from init_bot import ADMIN_ID

from keyboards.register import kb_accept


async def send_adm(msg: str, username: str, user_id: str):
	text = msg
	await bot.send_message(chat_id=ADMIN_ID, text="TEST text!\n" + text, reply_markup=kb_accept)
