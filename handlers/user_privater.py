from aiogram.filters import CommandStart,Command
from aiogram import types,Router,F
from keybords import reply,inline


user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("""Привет!Этот бот для продажи <s>людей</s>.""", reply_markup=reply.main_kb)



@user_router.message(F.text.lower().contains("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("вы открыли каталог!", reply_markup=reply.catalog_kb)


@user_router.message(F.text.lower() =="корзина")
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
        await callback.message.answer("оформить заказ на сайте.Выберите нужный товар и его количество нажмите кнопку «Добавить в корзину».Перейдите в раздел «Корзина».")
    elif quori =="2":
        await callback.message.answer("Экспресс-доставка из магазина по Минску.Вы можете получить свой заказ в течение 2 часов.Условия доставки:.Стоимость экспресс-доставки от 3,5 BYN. При заказе на сумму менее 50 BYN стоимость экспресс-доставки суммируется к стоимости стандартной доставки.Интервалы доставки: с 10:00 до 22:00.")
    elif quori =="3":
        await callback.message.answer("Безналичный расчет.Оплата онлайн-заказа банковской картой осуществляется на сайте при оформлении заказа.")
    await callback.answer("ответ отправлен")

@user_router.message(F.text.lower()== "назад")
async def back_menu(message: types.Message):
    await message.answer("главное меню", reply_markup=reply.main_kb)

# @user_router.message(F.text.lower().contains("стои")|F.text.lower().contains("цен"))
# async def echo(message: types.Message):
#     await message.answer("временно недоступен")
