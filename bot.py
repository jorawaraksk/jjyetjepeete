from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import basic, ffmpeg, system, commands, compressor, tools

app = Client("video_compressor_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

basic.init(app)
ffmpeg.init(app)
system.init(app)
commands.init(app)
compressor.init(app)
tools.init(app)

print("Bot is running...")
app.run()
