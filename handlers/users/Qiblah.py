from aiogram.types import Message
from loader import dp
from keyboards.inline.savolqibla import Qibla, islomdinimizsavol, Savolbot
from keyboards.default.menu import bekor2, Menu, Savolb
from keyboards.default.foydali import Savol
from states.savol import PersonalData2
from aiogram.dispatcher import FSMContext
from aiogram import types
import requests
import json

@dp.message_handler(text= "↩️ Orqaga",state=PersonalData2.adss2)
async def cancel1(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=Savolb)

@dp.message_handler(text= "Orqaga ↪️")
async def cancel2(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=Savol)
	
	
@dp.message_handler(text="🧭 Qibla Kompus")
async def select_Qibla(message: Message):
    qibla_id = "AgACAgIAAxkBAAIP8mIaMPMMCmAuwJtZKjnyd3HpvdQ5AALfvzEb6tXRSJY970crRxY7AQADAgADeQADIwQ"
    await message.answer_photo(qibla_id, caption=f"<b>🧭 Qibla Kompus Bo'lmidasiz.\n\n🕋 Qibla Qaysi Tarafda ekanligini aniqlash uchun 📍Joylashuv Yani (Location) ni Yoqing Va 👇Pastagi 🌐Saytga O'tish Tugmasni Bosing Va Sayt Sizga 🕋Qibla Qaysi Tarafda Ekanligini Aniqlab Beradi!\n\n✅ @islom_namoz_bot</b>",reply_markup=Qibla)
    
@dp.message_handler(text="🗞 Manbalar")
async def select_Manba(message: Message):
	await message.answer("<b>🤖 Botmizdagi Barcha Malumotlar ishonarli Sayt va Kanallardan Olindi.\n\n🗞 Biz Foydalangan Ⓜ️anbalar\n\n🌐 islom.uz\n🌐 islom.ziyouz.com\n🌐 YouTube.com\n🌐 savollar.islom.uz\n🌐 @Rafiqov_Afzal\n🌐 @Mishariy_Roshid_Alafasiy\n\n✅ @islom_namoz_bot</b>")
	
@dp.message_handler(text="📖 Dinimiz bo'yicha Savol")
async def islomsavol(message: Message):
    savolyi = "AgACAgIAAxkBAAInZGIo3WVVx2QFMROPSm_8N6XrxBdRAAIjvjEb9URJSUjqv4slytlcAQADAgADeAADIwQ"
    await message.answer_photo(savolyi,caption="<i>🤖 Ushbu bo'limda siz yo'lagan savolga o'xshash savollar savollar.islom.uz Saytiga yo'langan bo'lsa o'sha sizning savolingizga o'xshash Savol va Savol Javobi Sizga yuboriladi va o'sha sizning savolingizga o'xshash savolni o'qib chiqib Savolingizga Javob olasiz✅\n\n✅ @islom_namoz_bot</i>",reply_markup=Savolb)
	
@dp.message_handler(text="🤖 Bot bo'yicha Savol")
async def botsavol(message: Message):
	await message.answer("<b>🤖 Bot bo'yicha Savollaringiz bo'lsa quydagi Botga Yo'lashingiz Mumkun👇</b>",reply_markup=Savolbot)