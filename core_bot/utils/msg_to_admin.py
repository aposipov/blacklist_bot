from main import bot
from init_bot import ADMIN_ID

from keyboards.register import kb_accept


async def send_adm(msg: str, userid: str, name: str):
	text = msg
	if name is None:
		name = 'null'
	await bot.send_message(chat_id=ADMIN_ID, text="text:\n" + text + "\n"
	                       + "id: " + userid + "\n"
	                       + "usename: " + name, reply_markup=kb_accept)
