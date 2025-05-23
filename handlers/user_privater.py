from aiogram.filters import CommandStart,Command
from aiogram import types,Router,F
from keybords import reply,inline


user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет!Этот бот для продажи людей.", reply_markup=reply.main_kb)



@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("вы открыли каталог!", reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower().contains("корзина"))
@user_router.message(Command("cart"))
async def cart(message: types.Message):
    await message.answer("вы открыли корзину!")



@user_router.message(F.text.lower().contains("избранное"))
@user_router.message(Command("favorites"))
async def favorites(message: types.Message):
    await message.answer("вы открыли избранное!")


@user_router.message(F.text.lower().contains("вопросы"))
@user_router.message(Command("donating"))
async def donating(message: types.Message):
    await message.answer("частые вопросы",reply_markup=inline.question())

@user_router.callback_query(F.data.lower().startswith("question"))
async def answer(callback:types.CallbackQuery):
    quori = callback.data.split("_")[1]
    if quori == "1":
        await callback.message.answer("первый ответ")
    elif quori =="2":
        await callback.message.answer("второй ответ")
    elif quori =="3":
        await callback.message.answer("третий ответ")
    await callback.answer("ответ отправлен")

@user_router.message(F.text.lower()== "назад")
async def back_menu(message: types.Message):
    await message.answer("главное меню", reply_markup=reply.main_kb)

# @user_router.message(F.text.lower().contains("стои")|F.text.lower().contains("цен"))
# async def echo(message: types.Message):
#     await message.answer("временно недоступен")
