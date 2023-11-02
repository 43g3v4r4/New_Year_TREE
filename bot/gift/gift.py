from aiogram import types, Dispatcher
import os
from config import ADMINS, SQLITE_PATH
from db.db import connector_db_sqlite
from loader import dp


class Gift:
    def __init__(self, message: types.message):
        self.path_gift = os.path.join(f'{os.getcwd()}/gift/users')
        self.message_text = '<b>🎄🎄🎄  С новым годом! 🎄🎄🎄 \n\nДедушка Мороз положил тебе под ёлочку подарок =)</b>'
        self.message_text_not_gift = '<b>🎄🎄🎄 С новым годом! 🎄🎄🎄\n\nТы уже получил подарок от Дедушки Мороза или он положил его под другую ёлочку =)</b>'
        self.message_text_received_gift = '<b>Приходи в следующем году!</b>'

        self.message = message
        self.user_id = message.from_user.id

    async def is_received_gift(self):
        users_id = await connector_db_sqlite(
            base=SQLITE_PATH,
            query=f'SELECT user_id FROM received_gift WHERE user_id = {self.user_id}',
            data='',
        )

        if users_id[1]:
            return True
        else:
            return False

    async def set_received_gift(self):
        await connector_db_sqlite(
            base=SQLITE_PATH,
            query=f'INSERT INTO received_gift (user_id) VALUES ({self.user_id})',
            data='',
        )

    def check_gift(self):
        return os.path.exists(os.path.join(f'{self.path_gift}/{self.user_id}', 'gift.jpg'))

    @staticmethod
    async def tg_notification(text: str):
        for admin in ADMINS:
            await dp.bot.send_message(
                chat_id=admin,
                text=text)

    async def send(self):
        is_received_gift = await self.is_received_gift()

        if not is_received_gift:
            await dp.bot.send_sticker(
                chat_id=self.user_id,
                sticker='CAACAgIAAxkBAAEKqIdlQmXS0tH4Znmla958MeNpr5Rv6gACswsAAipQUUoso7YJ7GnT1jME',
            )

            if self.check_gift():
                await dp.bot.send_message(
                    chat_id=self.user_id,
                    text=self.message_text,
                )

                with open(f'{self.path_gift}/{self.user_id}/gift.jpg', 'rb') as photo:
                    await dp.bot.send_photo(
                        chat_id=self.user_id,
                        photo=photo,
                    )

                text = f'Пользователь {self.user_id} || {self.message.chat.first_name} {self.message.chat.last_name} || @{self.message.chat.username} - Получил подарок!'
                await self.tg_notification(text=text)

            else:
                await dp.bot.send_message(
                    chat_id=self.user_id,
                    text=self.message_text_not_gift,
                )
                text = f'Пользователь {self.user_id} || {self.message.chat.first_name} {self.message.chat.last_name} || @{self.message.chat.username} - Пытался получить подарок!'
                await self.tg_notification(text=text)

            await self.set_received_gift()
        else:
            await dp.bot.send_message(
                chat_id=self.user_id,
                text=self.message_text_received_gift,
            )
