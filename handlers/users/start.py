from keyboards.default import start
from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.username}!', reply_markup=start.start)
