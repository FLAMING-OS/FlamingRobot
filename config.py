# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Flaming-Music")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "pan_kaj_0027")
ALIVE_NAME = getenv("ALIVE_NAME", "FLAMING-MUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "TrickyAbhi_Music_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Flaming-Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "friendsforever431")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "friendsforever431")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/44089cf299cc80bba7c74.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SJMxADITI/HellMusic")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/596f75a52ea9bf0109644.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")

