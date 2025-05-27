import asyncio
from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN ="8175029494:AAErbnNXe7SjNMIy1m7iujgiZc_WibN5t7M"
bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

from handlers.catalog import catalog_router
from handlers.user_privater import user_router
from handlers.user_group import group_router
from handlers.catalog import catalog_router

dp.include_router(user_router)

dp.include_router(catalog_router)

dp.include_router(group_router)



async def main():
    print("бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())



















