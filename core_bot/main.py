import logging
import asyncio
import sys
from aiogram import Bot, Dispatcher
from init_bot import BOT_TOKEN, set_default
from handlers import start_handler, menu_search_handler, menu_blacklist_handler,\
    status_handler, adm_handlers, user_handlers

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def main():
    logging.info("BOT IS STARTED!")
    dp.include_router(start_handler.router)
    dp.include_router(user_handlers.router)
    dp.include_router(menu_search_handler.router)
    dp.include_router(menu_blacklist_handler.router)
    dp.include_router(adm_handlers.router)
    dp.include_router(status_handler.router)
    await set_default(bot)
    await dp.start_polling(bot)
    logging.info("STOP!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
