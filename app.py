from aiogram import Bot, Dispatcher, executor, types
from keyboards.default import user_main_menu, phone_share
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from sql.insert import insert_user
from sql.select import get_user

from states import RegisterState


token = "6076964790:AAGIIwBgUIWeWf3sZz87MrB2QaL6OIx1irQ"
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    user = await get_user(chat_id=message.chat.id)
    # if user:
    #     text = "Xush kelibsiz."
    #     await message.answer(text=text, reply_markup=user_main_menu)
    # else:
    text = f"Assalomu alaykum Ismingizni kiriting"
    await message.answer(text=text)
    await RegisterState.name.set()


@dp.message_handler(state=RegisterState.name)
async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    text = "Telefon raqamingizni kiriting"
    await message.answer(text=text, reply_markup=phone_share)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def number_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)

    text = "Iltimos Modme id kiriting"
    await message.answer(text=text)
    await RegisterState.modme_id.set()


@dp.message_handler(state=RegisterState.modme_id)
async def get_pass_hander(message: types.Message, state: FSMContext):
    await state.update_data(modme_id=message.text)
    text = "Modme parol kiriting."
    await message.answer(text=text)
    await RegisterState.modme_pass.set()


@dp.message_handler(state=RegisterState.modme_pass)
async def get_pass_handler(message: types.Message, state: FSMContext):
    await state.update_data(modme_pass=message.text, chat_id=message.chat.id)

    data = await state.get_data()
    await insert_user(data)


    text = "Ro'yxatdan o'tdingiz."
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()


@dp.message_handler(text="➕ Maxsulot qo'shish")
async def add_product_handler(message: types.Message):
    text = "Mahsulot malumotlarini kiriting."
    await message.answer(text=text)


@dp.message_handler(text="🚀 Mahsulotlar")
async def my_roducts_handler(message: types.Message):
    text = "Siz xali mahsulot qo'shmagansiz."
    await message.answer(text=text)



@dp.message_handler(text="🏪 Mars bozor")
async def support_handler(message: types.Message):
    text = "Mahsulotlar mavjud emas."
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