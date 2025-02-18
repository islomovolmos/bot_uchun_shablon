from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton


menu_start=InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Barcha kinolar\n",callback_data="kinolar"),
            InlineKeyboardButton(text="kino qidirish🎬\n",callback_data="qidirish"),
        ],
        [
            InlineKeyboardButton(text="valyutalar📊\n",callback_data="pul"),
            InlineKeyboardButton(text="kuchuklarning rasmari🐩\n",callback_data="rasm"),
        ],

    ],
     resize_keyboard=True
)
