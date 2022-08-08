from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Проверить баллы'),
        ],
    ],

    resize_keyboard=True
    # one_time_keyboard=True
)
