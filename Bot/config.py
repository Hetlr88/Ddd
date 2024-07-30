
import os
from pyrogram.types import BotCommand
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help message'),
        BotCommand('caption', 'custom caption'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('ban', 'ban user'),
        BotCommand('unban', 'unban user'),
        BotCommand('broadcast', 'broadcast message')
    ]

    DUMP_ID = int(os.environ.get("DUMP_ID",-1002205938557))

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6477025864:AAEf0VvMMlpNnR99ogHbFa3Z-jTXkZx7f24")

    APP_ID = int(os.environ.get("APP_ID", 13384432))
    API_HASH = os.environ.get("API_HASH","ea9db4503ed7088b788e06dfd818e00e")

    # Authorized User IDS
    AUTH_USERS = [int(id) for id in os.environ.get(
        "AUTH_USERS", "").split()] if os.environ.get("AUTH_USERS", None) else None

    OWNER_ID = int(os.environ.get('OWNER_ID',"6169288210"))

    # MongoDB
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://mrhex86:mrhex86@cluster0.8pxiirj.mongodb.net/?retryWrites=true&w=majority")

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://c.top4top.io/p_3125nmskm0.png")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # watermark file
    DEF_WATER_MARK_FILE = "@X_XF8"

    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
