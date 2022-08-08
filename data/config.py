import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

# webhook settings
WEBHOOK_HOST = str(os.getenv('WEBHOOK_HOST'))
WEBHOOK_PATH = f'/webhook/'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=4000)

admins = str(os.getenv('ADMINS'))
