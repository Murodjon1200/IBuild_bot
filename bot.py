import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = '6753119471:AAGnUZgvgo5DZ7USqUeZF_fUxTxfu1cXgQw'
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
from keyboards.default import isimlar 

@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(f" Asalomu Aleykum {message.from_user.first_name} <B>I BUILD</B> KAMPANIYASI ga xush kelibsiz😊", reply_markup=isimlar)



@dp.message_handler(text='🏢 Kompaniya Haqida')
async def file_sender_oqilxon(message: types.Message):
    with open('photo_ibuil.png', 'rb') as file:
        await message.answer_photo(file, caption="""
<B>I BUILD</B> kompaniyasi 2014-yilda tashkil topgan.
<B>I BUILD</B> kompaniyasini 4 ta inson ochgan: Odilov Toyrxo'ja, Isakov Mansurjon, Umaraliyev Fathulla, Mirvosilov Mirjalol.
<B>I BUILD</B> kompaniyasi offisi Yunsaboda joylashgan.
<B>I BUILD</B> kompaniyasi 500 dan ortiq 🏢 binolar qurib bitqizlilgan va 150 dan ortiq malakali 👷‍♂️mutahasislar bor.

        """, reply_markup=isimlar)


# @dp.message_handler(text='🏢 Kompaniya Haqida')
# async def oqilxon(message:types.Message):
#     await message.answer("""
#
# <B>I BUILD</B> kompaniyasi 2014-yilda tashkil topgan.
# <B>I BUILD</B> kompaniyasini 4 ta inson ochgan: Odilov Toyrxoja, Isakov Mansurjon, Umaraliyev Fathulla, Mirvosilov Mirjalol.
# <B>I BUILD</B> kompaniyasi offisi Yunsaboda joylashgan.
# <B>I BUILD</B> kompaniyasi 500 dan ortiq 🏢 binolar qurib bitqizlilgan va 150 dan ortiq malakali 👷‍♂️mutahasislar bor.
#
#
#     """, reply_markup=isimlar)





# @dp.message_handler(text='📞 Murojat uchun')
# async def murojat(message:types.Message):
#     await message.answer("""
#     ☎️Kontakt: +998 99 822 85 00, +998 99 861 12 00.
#     📍 Manzil: Yunusobod....... .
#     🔗Telegram manzil: https://t.me/Ibuild_uz
#     🔗Instagram manzil: ........ .
#     """)

@dp.message_handler(text='📞 Murojat uchun')
async def file_sender_oqilxon(message: types.Message):
    with open('photo_ibuil.png', 'rb') as file:
        await message.answer_photo(file,caption="""
    ☎️Kontakt: +998 99 822 85 00, 
                +998 99 861 12 00.
    📍 Manzil: Yunusobod....... .
    🔗Telegram manzil: https://t.me/Ibuild_uz
    🔗Instagram manzil: ........ .
        """)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
