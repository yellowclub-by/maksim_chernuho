from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
def question():
    builder = InlineKeyboardBuilder()
    builder.row(
    InlineKeyboardButton(text="1.Как сделать заказ",callback_data="question_1"),
            InlineKeyboardButton(text="2.Доставка заказа",callback_data="question_2"),
            InlineKeyboardButton(text="3.Оплата заказа",callback_data="question_3"),
    width=1
)
    return builder.as_markup()


links_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="сайт",url="https://vm.tiktok.com/ZMSNmLUr5/"),
            InlineKeyboardButton(text="тг",url="tg.//resolve?domain=danya_chaika")
        ]
    ]
)










