from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("➕ Maxsulot qo'shish"),
            KeyboardButton("🚀 Mahsulotlar")
        ],
        [
            KeyboardButton("👤 Profil"),
            KeyboardButton("📞 Aloqa")
        ]
    ], resize_keyboard=True
)