from aiogram.filters import CommandStart,Command
from aiogram import types,Router,F

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет!Этот бот для продажи людей.")



@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("вы открыли каталог!")


@user_router.message(F.text.lower().contains("корзина"))
@user_router.message(Command("cart"))
async def cart(message: types.Message):
    await message.answer("вы открыли корзину!")



@user_router.message(F.text.lower().contains("избранное"))
@user_router.message(Command("favorites"))
async def favorites(message: types.Message):
    await message.answer("вы открыли избранное!")


@user_router.message(F.text.lower().contains("донат  "))
@user_router.message(Command("donating"))
async def donating(message: types.Message):
    await message.answer("вы хотите пожертвовать в наш бот?")

@user_router.message(F.text.lower().contains("стои")|F.text.lower().contains("цен"))
async def echo(message: types.Message):
    await message.answer("временно недоступен")
