import asyncio
from aiogram import Bot,Dispatcher,types

TOKEN ="8175029494:AAErbnNXe7SjNMIy1m7iujgiZc_WibN5t7M"
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message()
async def echo(message: types.Message):
    await message.answer("временно недоступен")



async def main():
    print("бот запущен")
    await dp.start_polling(bot)

asyncio.run(main())