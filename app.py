from aiogram import executor

from loader import dp, bot
# import handlers, keyboards
# from utils.notify_admins import on_startup_notify
from utils.commands.bot_commands import set_all_default_commands
from data.config import (WEBHOOK_URL, WEBHOOK_PATH,
                         WEBAPP_HOST, WEBAPP_PORT)


async def on_startup(dispetcher):
    await set_all_default_commands(dispetcher.bot)
    # await on_startup_notify(dispetcher)
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispetcher):
    await bot.delete_webhook()


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
