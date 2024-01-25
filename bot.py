
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

async def start():
    await start()
    usr_bot_me = await get_me()
    uptime = datetime.now()

    if FORCE_SUB_CHANNEL:
        try:
            link = (await get_chat(FORCE_SUB_CHANNEL)).invite_link
            if not link:
                await export_chat_invite_link(FORCE_SUB_CHANNEL)
                link = (await get_chat(FORCE_SUB_CHANNEL)).invite_link
            invitelink = link
        except Exception as a:
            LOGGER(__name__).warning(a)
            LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
            LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
            exit()
        try:
            db_channel = await get_chat(CHANNEL_ID)
            db_channel = db_channel
            test = await send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            LOGGER(__name__).warning(e)
            LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            sys.exit()

        set_parse_mode(ParseMode.HTML)
        LOGGER(__name__).info(f"Bot Started..!")
        username = usr_bot_me.username
        
async def stop(*args):
    await super().stop()
    LOGGER(__name__).info("Bot stopped.")


if __name__ == "__main__":   
    bot.run()