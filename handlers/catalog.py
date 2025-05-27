from aiogram import types,Router,F
from aiogram.types import FSInputFile
catalog_router = Router()
@catalog_router.message(F.text.lower()== "апельсины")
async def first_position(message: types.Message):
    photo = FSInputFile("img/catalog/orange.jpg")
    await message.answer_photo  (photo)
    await message.answer("Апельсин – это цитрусовый фрукт, представляющий собой многогнёздную ягоду (гесперидий), покрытую шероховатой оранжевой кожурой (цедрой). Внутри апельсина находятся сегменты мякоти, содержащие сок и семена. Апельсины имеют округлую или слегка вытянутую форму, их размер и форма могут варьироваться в зависимости от сорта")


@catalog_router.message(F.text.lower()== "кокосы")
async def second_position(message: types.Message):
    photo = FSInputFile("img/catalog/cocanat.jpg")
    await message.answer_photo  (photo)
    await message.answer("Кокос – это плод кокосовой пальмы, относящийся к семейству Пальмовые. Он представляет собой крупную, волокнистую костянку, или, как ее еще называют, «сухая костянка», окруженной жесткой скорлупой и волокнами. Внутри кокоса находится мякоть, окруженная жидкостью, известной как кокосовая водa")
@catalog_router.message(F.text.lower() == "чернослив")
async def third_position(message: types.Message):
        photo = FSInputFile("img/catalog/chernosliw.jpg")
        await message.answer_photo(photo)
        await message.answer("Чернослив – это сухофрукт, полученный из темных сортов сливы, особенно высушенных на солнце. Плоды чернослива обычно имеют тёмно-фиолетовый или почти чёрный цвет, глянцевую поверхность и слегка липкую текстуру. Вкус чернослива сладкий с лёгкой кислинкой")


@catalog_router.message(F.text.lower() == "питахайя")
async def fourth_position(message: types.Message):
        photo = FSInputFile("img/catalog/pitahaya.jpg")
        await message.answer_photo(photo)
        await message.answer("Питахайя, также известная как драконий фрукт или клубничная груша, – это плод некоторых видов кактусов, в основном рода Hylocereus. Это экзотический фрукт, который привлекает внимание своей необычной внешностью, напоминающей большую шишку с чешуйками")