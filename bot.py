
import pyromod.listen
from pyrogram import Client as Bot
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, API_ID, LOGGER, BOT_TOKEN, BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.INFO)

bot = Bot(
    name='bot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)
        
async def stop(*args):
    await super().stop()
    LOGGER(__name__).info("Bot stopped.")


if __name__ == "__main__":   
    bot.run()
