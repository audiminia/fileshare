import os
import logging
from logging.handlers import RotatingFileHandler

import dotenv
from os import getenv

dotenv.load_dotenv('config.env')


#Your API ID from my.telegram.org
API_ID = int(getenv("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = getenv("API_HASH", "")

#Bot token @Botfather
BOT_TOKEN = getenv("BOT_TOKEN", "")

#Your db channel Id
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(getenv("OWNER_ID", ""))

#Port
PORT = getenv("PORT", "8080")

#Database 
DB_URI = getenv("DATABASE_URL", "")
DB_NAME = getenv("DATABASE_NAME", "FileCopying")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(getenv("FORCE_SUB_CHANNEL", "0"))

BOT_WORKERS = int(getenv("TG_BOT_WORKERS", "4"))

#start message
START_MSG = getenv("START_MESSAGE", "Hello {first}\n\nI share file so the users can access it from link.")
try:
    ADMINS=[]
    for x in (getenv("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = getenv("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if getenv('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = getenv("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filecopying.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
