from init_bot import ADMIN_ID, GROUP_ID, TH_SUPPORT, TH_UPLOAD, TH_REGISTRATION
from keyboards.kb_register import kb_accept

from aiogram.types import Message


async def send_adm(msg: str, userid: str, name: str, fullname: str, icode: str):
	from main import bot
	uname = name
	if uname is None:
		uname = 'null'
	uname = "@" + uname
	await bot.send_message(chat_id=GROUP_ID, text=userid, message_thread_id=TH_REGISTRATION)
	await bot.send_message(chat_id=GROUP_ID, text="ID: " + userid + "\n"
	                    + "usename: " +  uname + "\n"
	                    + "fullname: " + fullname + "\n"
	                    + "ICODE: " + icode + "\n"
	                    + "text:\n" + msg + "\n",
	                    # reply_markup=kb_accept,
	                    message_thread_id=TH_REGISTRATION)


async def send_from_support(msg: Message):
	from main import bot
	uname = msg.from_user.username
	userid = str(msg.from_user.id)
	if msg.from_user.username is None:
		uname = 'null'
	uname = "@" + uname
	await bot.send_message(chat_id=GROUP_ID, text=userid, message_thread_id=TH_SUPPORT)
	await bot.send_message(chat_id=GROUP_ID,
	                       text="ID: " + userid+ "\n"
	                       + "uname: " + uname + "\n"
	                       + "***\n"
	                       + msg.text,
	                       message_thread_id=TH_SUPPORT)


async def file_was_sent(msg: Message):
	from main import bot
	filename = msg.document.file_name
	userid = str(msg.from_user.id)
	await bot.send_message(chat_id=GROUP_ID,
	                       text="ID: " + userid + "\n"
	                            + "File (" + filename + ") was sent!",
	                       message_thread_id=TH_UPLOAD)
