from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from utils.misc.request import req


@dp.message_handler(Command('score'))
async def cmd_score(message: Message, msg=''):
    for i, item in enumerate(req()):
        msg += f'[{i+1}] - {item[1]}\n' \
               f'Набрано баллов - {item[2]}\n'
    await message.answer(msg)
