import asyncio
from aiogram import Bot,Dispatcher



TOKEN ="8175029494:AAErbnNXe7SjNMIy1m7iujgiZc_WibN5t7M"
bot = Bot(token=TOKEN)
dp = Dispatcher()

from handlers.user_privater import user_router
dp.include_router(user_router)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())



















