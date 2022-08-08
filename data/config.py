import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
APP_URL = str(os.getenv('APP_URL')) + BOT_TOKEN

admins = str(os.getenv('ADMINS'))
