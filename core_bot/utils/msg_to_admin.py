from main import bot
from init_bot import ADMIN_ID

from keyboards.kb_register import kb_accept


async def send_adm(msg: str, userid: str, name: str, fullname: str, icode: str):
	if name is None:
		name = 'null'
	await bot.send_message(chat_id=ADMIN_ID, text=userid)
	await bot.send_message(chat_id=ADMIN_ID, text="ID: " + userid + "\n"
	                    + "usename: " + name + "\n"
	                    + "fullname: " + fullname + "\n"
	                    + "ICODE: " + icode + "\n"
	                    + "text:\n" + msg + "\n",
	                    reply_markup=kb_accept)
