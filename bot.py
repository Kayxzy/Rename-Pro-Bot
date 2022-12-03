#-------------------------------------- https://github.com/dakshkohli23/Rename-Pro-Bot --------------------------------------#

import logging
import os
import sys
from pyrogram import Client
from pyrogram.raw.all import layer
from translation import Translation

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


# noinspection PyAttributeOutsideInit
class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name="Dlaize",
            bot_token=Config.TG_BOT_TOKEN,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            plugins={"root": "plugins"},
        )

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.Translation.START_APP_TEXT(__name__).format(
                f"START_APP_TEXT detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            )
            sys.exit()

    async def stop(self, *args):
        await super().stop()
        self.Translation.START_APP_TEXT(__name__).format("Bot stopped.")

app = Bot()
app.run()
