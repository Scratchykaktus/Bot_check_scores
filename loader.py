from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from flask import Flask, request

from data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

server = Flask(__name__)
bot.delete_webhook()
bot.set_webhook(url=config.APP_URL)

logging.basicConfig(level=logging.INFO)
