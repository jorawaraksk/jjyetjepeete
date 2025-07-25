from pyrogram import filters
from pyrogram.types import Message
import os

def init(app):
    @app.on_message(filters.command("renew"))
    async def renew(_, msg: Message):
        os.system("rm -rf downloads/*")
        await msg.reply("♻️ Cleared downloads.")

    @app.on_message(filters.command("clear"))
    async def clear(_, msg: Message):
        os.system("rm -rf queue/*")
        await msg.reply("🧹 Queue cleared.")

    @app.on_message(filters.command("logs"))
    async def logs(_, msg: Message):
        await msg.reply_document("bot.log")

    @app.on_message(filters.command("showthumb"))
    async def show_thumb(_, msg: Message):
        if os.path.exists("thumb.jpg"):
            await msg.reply_photo("thumb.jpg")
        else:
            await msg.reply("No thumbnail set.")
