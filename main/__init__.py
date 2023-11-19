#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28414908
API_HASH = "8d2e5bdb8848ae0b37e869be445a8f32"
BOT_TOKEN = "6596482531:AAHmCTDtxYMflOgT4hmSV7LBNqkEh8IQGrE"
SESSION = "AQAhIHQAZpPbeZrVmZxDble8MiIPmbVmGmbBcOx4fHzxJCgeBinsLYzS3l3tppwmHv5XeDgmeGSzVFf8z7McSTEH4YLUAgXkisk44Tn5t0dsTjrQiFVbQWeZyurR0Hja5egYhI0NkwdXPoV9GAbckQGhBrvNFdqE4ws_hQ6vwY7agE8Q2xLQoC-MnZl8xzEl2VoxFPm0jk4Jgr0AeHrZJkkaKn2VVjRE6NQqJsKc3tEBnrTAOUiUC2BjJz9XQPsEZbo3seauUQo_umRU0DTiNJ-MuFtEgezCd7ejW6tMSPYiDnZH1tpk03h6ur5MY5LcHGMSkZkiW1Zr5jMvLZUQqvO7PqESswAAAABuJAClAA"
FORCESUB = "lepinst4r"
AUTH = "1847853221"

auth = config("AUTH", default=None, cast=int)
ids = auth.split(",")
for id in ids:
    AUTH.append(int(id))
    
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
