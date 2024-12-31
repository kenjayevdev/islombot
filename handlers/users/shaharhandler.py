import logging
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.shahar import orqaga
from keyboards.inline.menuin import categoryMenu
import requests
import json
import datetime
import pytz
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.answer(f"<b>🕌 Marhamat kerakli viloyatni Tanlang!</b>",reply_markup=categoryMenu)
    await call.message.delete()

def soat():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
    dt_time = pst_now.strftime("%H:%M:%S")
    return dt_time

def year():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
    dt_year = pst_now.strftime("%d.%m.%Y-YIL")
    return dt_year
	
@dp.callback_query_handler(text="27")
async def toshkent(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=toshkent"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Toshkent Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="43")
async def Angren(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Angren"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Angren Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="2")
async def Bekobod(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Bekobod"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Bekobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
 
@dp.callback_query_handler(text="1")
async def Andijon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Andijon"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Andijon Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="31")
async def Xonobod(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Xonobod"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Xonobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="28")
async def Shahrixon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Shahrixon"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Shahrixon Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="29")
async def Xojaobod(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Xo%27jaobod"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Xo'jaobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="37")
async def Fargona(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Farg%27ona"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Farg'ona Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="13")
async def Margilon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Marg%27ilon"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Marg'ilon Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="26")
async def Qoqon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Qo%27qon"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Qo'qon Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="39")
async def Rishton(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Rishton"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Rishton Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="38")
async def Oltiariq(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Oltiariq"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Oltiariq Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="40")
async def Quva(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Quva"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Quva Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="15")
async def Namangan(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Namangan"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Namangan Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="35")
async def Chortoq(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Chortoq"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Chortoq Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="33")
async def Chust(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Chust"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Chust Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="32")
async def Pop(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Pop"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Pop Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="36")
async def Uchqorgon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Uchqo%27rg%27on"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Uchqo'rg'on Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="5")
async def Guliston(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Guliston"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Guliston Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="49")
async def Paxtaobod(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Paxtaobod"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Paxtaobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="9")
async def Jizzax(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Jizzax"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Jizzax Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="50")
async def Zomin(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Zomin"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Zomin Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="55")
async def Gallaorol(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=G%27allaorol"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 G'allaorol Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="51")
async def Dostlik(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Do%27stlik"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Do'stlik Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="18")
async def Samarqand(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Samarqand"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Samarqand Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="11")
async def Kattaqorgon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Kattaqo%27rg%27on"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Kattaqo'rg'on Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="72")
async def Urgut(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Urgut"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Urgut Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="4")
async def Buxoro(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Buxoro"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Buxoro Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="46")
async def Gazli(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Gazli"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Gazli Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="48")
async def Qorakol(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Qorako%27l"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Qorako'l Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text="25")
async def Qarshi(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Qarshi"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Qarshi Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="84")
async def Dehqonobod(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Dehqonobod"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Dehqonobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="88")
async def Muborak(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Muborak"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Muborak Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="85")
async def Guzor(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=G%27uzor"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 G'uzor Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="74")
async def Termiz(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Termiz"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Termiz Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="76")
async def Boysun(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Boysun"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Boysun Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="6")
async def Denov(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Denov"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Denov Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="77")
async def Sherobod(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Sherobod"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Sherobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="75")
async def Qumqorgon(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Qumqo%27rg%27on"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Qumqo'rg'on Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="14")
async def Navoiy(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Navoiy"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Navoiy Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text="59")
async def Konimex(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Konimex"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Konimex Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="17")
async def Nurota(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Nurota"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Nurota Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="63")
async def Uchquduq(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Uchquduq"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Uchquduq Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="78")
async def Urganch(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Urganch"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Urganch Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="79")
async def Xazorasp(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Xazorasp"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Xazorasp Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="80")
async def Xonqa(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Xonqa"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Xonqa Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="82")
async def Shovot(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Shovot"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Shovot Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="21")
async def Xiva(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Xiva"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Xiva Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="16")
async def Nukus(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Nukus"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Nukus Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="68")
async def Moynoq(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Mo%27ynoq"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Mo'ynoq Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text="66")
async def Taxtakopir(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Taxtako%27pir"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Taxtako'pir Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="65")
async def Tortkol(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=To%27rtko%27l"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 To'rtko'l Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="71")
async def Qongirot(call: CallbackQuery):
    url = "https://islomapi.uz/api/present/day?region=Qo%27ng%27irot"
    response = requests.get(url)
    data_from_url = response.json()

    bomdod = data_from_url["times"]["tong_saharlik"]
    peshin = data_from_url["times"]["peshin"]
    asr = data_from_url["times"]["asr"]
    shom = data_from_url["times"]["shom_iftor"]
    xufton = data_from_url["times"]["hufton"]
    await call.message.answer(f"<b>🕌 Qo'ng'irot Shahri\n➖➖➖➖➖➖\n📆 Bugun - {year()}\n⏰ Soat - {soat()}\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
soat()
year()