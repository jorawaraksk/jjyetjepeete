from pyrogram import filters
from pyrogram.types import Message
from utils.compress import compress_video
import os

def init(app):
    @app.on_message(filters.command("leech"))
    async def leech(_, msg: Message):
        if len(msg.command) < 2:
            return await msg.reply("❌ Usage: /leech <URL>")

        url = msg.text.split(maxsplit=1)[1]
        await msg.reply("⏬ Downloading video...")

        # TODO: Replace this with actual download logic
        filename = "sample.mp4"
        if not os.path.exists(filename):
            return await msg.reply("❌ Failed to download video.")

        await msg.reply("🎥 Compressing video...")
        output = await compress_video(filename)

        if not output or not os.path.exists(output):
            return await msg.reply("❌ Compression failed. Check your ffmpeg code or source file.")

        await msg.reply("📤 Uploading compressed video...")
        await msg.reply_video(output)

        os.remove(filename)
        os.remove(output)
