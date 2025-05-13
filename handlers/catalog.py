from aiogram import types,Router,F
from aiogram.types import FSInputFile
catalog_router = Router()
@catalog_router.message(F.text.lower()== "апельсины")
async def first_position(message: types.Message):
    photo = FSInputFile("img/catalog/orange.jpg")
    await message.answer_photo  (photo)
    await message.answer("первый товар")


@catalog_router.message(F.text.lower()== "кокосы")
async def second_position(message: types.Message):
    photo = FSInputFile("img/catalog/cocanat.jpg")
    await message.answer_photo  (photo)
    await message.answer("второй товар")
@catalog_router.message(F.text.lower() == "чернослив")
async def third_position(message: types.Message):
        photo = FSInputFile("img/catalog/chernosliw.jpg")
        await message.answer_photo(photo)
        await message.answer("третий товар")


@catalog_router.message(F.text.lower() == "питахайя")
async def fourth_position(message: types.Message):
        photo = FSInputFile("img/catalog/pitahaya.jpg")
        await message.answer_photo(photo)
        await message.answer("четвертый товар")