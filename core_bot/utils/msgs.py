
async def msg(userid: int, text: str):
	from main import bot
	await bot.send_message(chat_id=userid, text=text)
