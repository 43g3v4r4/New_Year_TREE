from aiogram import types
import keyboards as kb
from gift.gift import Gift
from loader import dp
from config import ADMINS


# Обработчик текстовых команд
@dp.message_handler(content_types=['text'])
async def text(message: types.message):
    command = message.text.strip()

    if command == 'Заглянуть под Ёлочку':
        await Gift(message=message).send()
        #await dp.bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEKqIdlQmXS0tH4Znmla958MeNpr5Rv6gACswsAAipQUUoso7YJ7GnT1jME')

        await message.delete()

    else:
        await message.answer('Нажми на любую из кнопок или введи /start!')
