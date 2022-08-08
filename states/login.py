from aiogram.dispatcher.filters.state import StatesGroup, State


class Login(StatesGroup):
    InputLogin = State()
    InputPassword = State()
