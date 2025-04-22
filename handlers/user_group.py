from aiogram.filters import CommandStart,Command
from aiogram import types,Router,F

group_router = Router()

no_words = ["черемша","тюрьма","кокос","свага отсутствует","макан  "]


@group_router.message(F.text)
async def conceled_worlds(message:types.Message):
   user_words =  message.text.split(" ")
   for word in user_words:
       if word.lower() in no_words:
           await message.answer(f"{message.from_user.first_name} тебя ждут спортики под дверью)")
           await message.delete()
           break







