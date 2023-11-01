from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram import types


# Обработка inline кнопки "Отмена"
@dp.callback_query_handler(lambda c: c.data == 'back_setting_matrix', state='*')
async def callback_button_back_stocks_file(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.bot.send_message(
        chat_id=callback_query.from_user.id,
        text='Если понадоблюсь ещё, то клацай на кнопочки =)',
    )
    await state.finish()

    await dp.bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=None
    )
