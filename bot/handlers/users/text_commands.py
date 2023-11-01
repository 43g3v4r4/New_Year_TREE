from aiogram import types
import keyboards as kb
from loader import dp
from config import ADMINS



# Обработчик текстовых команд
@dp.message_handler(content_types=['text'])
async def text(message: types.message):
    command = message.text.strip()

    if command == 'Заглянуть под Ёлочку':
        await message.answer('<b>Твой подарок!</b>')

        await message.delete()

    else:
        await message.answer('Нажми на любую из кнопок или введи /start!')
