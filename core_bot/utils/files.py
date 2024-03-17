from aiogram.types import Message
import os


async def get_img(message: Message, driverid: str) -> str:
	from main import bot
	# send adm msg about file
	document = message.document
	# document
	ext = document.file_name.split(sep='.')
	driver_folder = f"data/files/{driverid}"
	if not os.path.isdir(driver_folder):
		os.mkdir(driver_folder)
	path_to_data = f"{driver_folder}/{driverid}_{str(message.from_user.id)}.{ext[1]}"
	await bot.download(document, path_to_data)
	print(path_to_data)
	return path_to_data
