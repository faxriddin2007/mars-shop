from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("➕ Maxsulot qo'shish"),
            KeyboardButton("🚀 Mahsulotlarim")
        ],
        [
            KeyboardButton("👤 Profil"),
            KeyboardButton("🏪 Mars bozor")
        ]
    ], resize_keyboard=True
)

phone_share = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton("📞 Raqamni yuborish", request_contact=True)
        ]
    ], resize_keyboard=True
)
