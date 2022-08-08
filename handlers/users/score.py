import logging

from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text

from utils.misc.request import req


@dp.message_handler(Command('score'))
async def cmd_score(message: Message, state: FSMContext):
    # data = await state.get_data()
    # login = await data.get('login')
    # pas = await data.get('password')
    #
    # if login == '':
    #     logging.info('Не верные данные')
    # else:
    msg = ''
    for i, item in enumerate(req()):
        msg += f'[{i+1}] - {item[1]}\n' \
               f'Набрано баллов - {item[2]}\n\n'
    await message.answer(msg)


@dp.message_handler(Text(equals=['Проверить баллы']))
async def cmd_score2(message: Message):
    msg = ''
    for i, item in enumerate(req()):
        msg += f'[{i+1}] - {item[1]}\n' \
               f'<b>Набрано баллов</b> - {item[2]}\n\n'
    await message.answer(msg)
