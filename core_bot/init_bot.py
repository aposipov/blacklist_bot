from environs import Env
from aiogram import Bot
from aiogram.types import BotCommand

env = Env()
env.read_env()
BOT_TOKEN = env.str('TOKEN')

# bot.set_my_description
greeting = "press /start I can add to bl"

# bot.set_my_short_description
about = "about this bot test"


# Функция для настройки кнопки Menu бота
async def set_menu(bot: Bot):
	cmds = [
		BotCommand(command="help", description="справка"),
		BotCommand(command="support", description="обратиться в поддержку"),
		BotCommand(command="status", description="test online"),
		BotCommand(command="test", description="test"),
	]
	await bot.set_my_commands(cmds)


async def set_default(bot: Bot):
	await set_menu(bot)
	await bot.set_my_description(greeting)
	await bot.set_my_short_description(about)
