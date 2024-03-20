from init_bot import ADMIN_ID
from keyboards.kb_register import kb_accept

from aiogram.types import Message


async def send_adm(msg: str, userid: str, name: str, fullname: str, icode: str):
	from main import bot
	uname = name
	if uname is None:
		uname = 'null'
	uname = "@" + uname
	await bot.send_message(chat_id=ADMIN_ID, text=userid)
	await bot.send_message(chat_id=ADMIN_ID, text="ID: " + userid + "\n"
	                    + "usename: " +  uname + "\n"
	                    + "fullname: " + fullname + "\n"
	                    + "ICODE: " + icode + "\n"
	                    + "text:\n" + msg + "\n",
	                    reply_markup=kb_accept)


async def send_from_support(msg: Message):
	from main import bot
	uname = msg.from_user.username
	userid = str(msg.from_user.id)
	if msg.from_user.username is None:
		uname = 'null'
	uname = "@" + uname
	await bot.send_message(chat_id=ADMIN_ID, text=userid)
	await bot.send_message(chat_id=ADMIN_ID,
	                       text="ID: " + userid+ "\n"
	                       + "uname: " + uname + "\n"
	                       + "***\n"
	                       + msg.text)


async def file_was_sent(msg: Message):
	from main import bot
	filename = msg.document.file_name
	userid = str(msg.from_user.id)
	await bot.send_message(chat_id=ADMIN_ID,
	                       text="ID: " + userid + "\n"
	                            + "File (" + filename + ") was sent!")