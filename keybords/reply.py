from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

back_btn =KeyboardButton(text="назад")

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="каталог"),KeyboardButton(text="корзина")],
        [KeyboardButton(text="избранное"),KeyboardButton(text="частые вопросы")]

    ],
    resize_keyboard=True,
    input_field_placeholder="привет, вас съест максим квадробер)"
)
catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="апельсины"),KeyboardButton(text="кокосы")],
        [KeyboardButton(text="чернослив"),KeyboardButton(text="питахайя")],
        [back_btn]
    ]
)