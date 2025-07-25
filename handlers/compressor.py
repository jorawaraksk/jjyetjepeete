from pyrogram import filters
from pyrogram.types import Message
from utils.compress import compress_video
import os

def init(app):
    @app.on_message(filters.video)
    async def compress_telegram_video(_, msg: Message):
        downloading = await msg.reply("📥 Downloading video...")

        # Download the video from Telegram
        input_path = await msg.download()

        await downloading.edit("🎬 Compressing video...")
        output_path = await compress_video(input_path)

        if output_path and os.path.exists(output_path):
            await downloading.edit("📤 Uploading compressed video...")
            await msg.reply_video(output_path)
            os.remove(output_path)
        else:
            await downloading.edit("❌ Compression failed.")

        os.remove(input_path)
