from pyrogram import filters
from pyrogram.types import Message
from utils.compress import compress_video
import os

def init(app):
    @app.on_message(filters.command("leech"))
    async def leech(_, msg: Message):
        url = msg.text.split(maxsplit=1)[-1]
        await msg.reply("⏬ Downloading video...")

        # Replace this part with yt-dlp integration or requests
        filename = "sample.mp4"  # Mocked for now

        output = await compress_video(filename)
        await msg.reply_video(output)
