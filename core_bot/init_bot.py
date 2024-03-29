from environs import Env
from aiogram import Bot
from aiogram.types import BotCommand

env = Env()
env.read_env()
BOT_TOKEN = env.str("TOKEN")
ADMIN_ID = env.str("ADMIN_ID")
GROUP_ID = env.str("GROUP_ID")
TH_SUPPORT = env.str("TH_SUPPORT")
TH_REGISTRATION = env.str("TH_REGISTRATION")
TH_UPLOAD = env.str("TH_UPLOAD")
DB_PATH = 'data/dev_blacklist.db'

# bot.set_my_description
greeting = "С помощью этого бота вы можете вести базу данных\n" \
			"ваших контрагентов.\n" \
			"Нажмите СТАРТ!"

# bot.set_my_short_description
about = "Бот поможет создать Базу Данных ваших Контрагентов."


# Функция для настройки кнопки Menu бота
async def set_menu(bot: Bot):
	cmds = [
		BotCommand(command="menu", description="основное меню"),
		BotCommand(command="help", description="справка"),
		BotCommand(command="support", description="обратиться в поддержку"),
		BotCommand(command="status", description="проверка доступности сервиса"),
	]
	await bot.set_my_commands(cmds)


async def set_default(bot: Bot):
	await set_menu(bot)
	await bot.set_my_description(greeting)
	await bot.set_my_short_description(about)
