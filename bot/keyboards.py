from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Заглянуть под Ёлочку"),
        ],
    ],
    resize_keyboard=True
)
