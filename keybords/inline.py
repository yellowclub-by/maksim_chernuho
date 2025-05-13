from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def question():
    builder = InlineKeyboardBuilder()
    builder.row(
    InlineKeyboardButton(text="1.вопрос",callback_data="question_1"),
            InlineKeyboardButton(text="2.вопрос",callback_data="question_2"),
            InlineKeyboardButton(text="3.вопрос",callback_data="question_3"),
    width=1
)
    return builder.as_markup()










