from aiogram import types

from loader import dp
from aiogram.dispatcher.filters import Command
import keyboards as kb


@dp.message_handler(Command("start"), state=None)
async def start(message: types.Message):
    await message.delete()
    await message.answer('Нажми на кнопку!', reply_markup=kb.menu)