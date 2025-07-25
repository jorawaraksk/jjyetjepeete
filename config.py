import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))
FFMPEG_CODE = os.getenv("FFMPEG_CODE", "-preset fast -crf 28")
LOG_FILE = "bot.log"
