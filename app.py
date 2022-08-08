import os

from aiogram import executor

from loader import dp, server
import handlers
# from utils.notify_admins import on_startup_notify
from utils.commands.bot_commands import set_all_default_commands


async def on_startup(dispetcher):
    await set_all_default_commands(dispetcher.bot)

    # await on_startup_notify(dispetcher)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
