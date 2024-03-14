from db.db_users import get_uids


async def msg(userid: int, text: str):
	from main import bot
	await bot.send_message(chat_id=userid, text=text)


async def shout(text: str):
	from main import bot
	u_ids = get_uids()
	for u in u_ids:
		print(u[0])
		try:
			await bot.send_message(chat_id=int(u[0]), text=text)
		except Exception as e:
			print(f'shout ERROR! {e}')
