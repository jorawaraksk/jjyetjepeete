from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID

current_code = None

def init(app):
    @app.on_message(filters.command("setcode") & filters.user(OWNER_ID))
    async def set_code(_, msg: Message):
        global current_code
        if len(msg.command) < 2:
            return await msg.reply("Usage: /setcode <ffmpeg options>")
        current_code = " ".join(msg.command[1:])
        await msg.reply(f"✅ Set FFMPEG code to:\n`{current_code}`")

    @app.on_message(filters.command("getcode"))
    async def get_code(_, msg: Message):
        global current_code
        await msg.reply(f"🎯 Current FFMPEG Code:\n`{current_code}`" if current_code else "No custom code set.")
