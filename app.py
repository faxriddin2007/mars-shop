from aiogram import Bot, Dispatcher, executor, types
from keyboards.default import user_main_menu
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


token = "6076964790:AAGIIwBgUIWeWf3sZz87MrB2QaL6OIx1irQ"
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = f"Assalomu alaykum {message.from_user.full_name}. Botimizga xush kelibsiz."
    await message.answer(text=text, reply_markup=user_main_menu)


@dp.message_handler(text="➕ Maxsulot qo'shish")
async def add_product_handler(message: types.Message):
    text = "Mahsulot malumotlarini kiriting."
    await message.answer(text=text)


@dp.message_handler(text="🚀 Mahsulotlar")
async def my_roducts_handler(message: types.Message):
    text = "Siz xali mahsulot qo'shmagansiz."
    await message.answer(text=text)



@dp.message_handler(text="📞 Aloqa")
async def support_handler(message: types.Message):
    text = "🧑‍💻 Aloqa uchun: @Faxriddinovv_7"
    await message.answer(text=text)



@dp.message_handler(text="👤 Profil")
async def profile_handler(message: types.Message):
    text = f"""
Ismingiz: {message.from_user.first_name}
Username: @{message.from_user.username}
"""
    await message.answer(text=text)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)