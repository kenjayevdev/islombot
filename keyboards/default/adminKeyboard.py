from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel = ReplyKeyboardMarkup(
    keyboard = [
         [
         KeyboardButton(text="📨 SEND MSG"),
         KeyboardButton(text="👤 ALL USERS"),
         ],
         [
         KeyboardButton(text="🤖BOT STATISTIKASI📊"),
         ],
         [
         	KeyboardButton(text="🔚MENU🔜"),
         ],
       ],
       resize_keyboard=True
)

bekor = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="Orqaga🔜"),
        ],
     ],
     resize_keyboard=True
)