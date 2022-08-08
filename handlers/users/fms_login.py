import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp
from states.login import Login


@dp.message_handler(Command('login'), state=None)
async def enter_data(message: Message):
    await message.answer(text='Для вывода баллов, сначала необходимо выполнить вход!')
    await message.answer('Введите ваш логин')

    await Login.InputLogin.set()


@dp.message_handler(state=Login.InputLogin)
async def input_login(message: Message, state: FSMContext):

    login = message.text

    async with state.proxy() as data:
        data['login'] = login

    await message.answer('Введите ваш пароль')

    await Login.next()


@dp.message_handler(state=Login.InputPassword)
async def input_password(message: Message, state: FSMContext):

    password = message.text

    async with state.proxy() as data:
        data['password'] = password

    await state.reset_state(with_data=False)
    await message.answer('Теперь можете посмотреть ваши баллы - /score')
