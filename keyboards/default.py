from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

isimlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🏢 Kompaniya Haqida'),
        ],
        [
            KeyboardButton('📞 Murojat uchun')
        ],
        [
            KeyboardButton('📍 Fililallar')
        ],
        [
            KeyboardButton("💼Bo'sh ish orinlar")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)




