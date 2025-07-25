from pyrogram import filters
from pyrogram.types import Message

def init(app):
    @app.on_message(filters.command("start"))
    async def start(_, msg: Message):
        await msg.reply("🤖 Bot is alive!")

    @app.on_message(filters.command("help"))
    async def help(_, msg: Message):
        await msg.reply("Send a video or use /leech <url> to compress.\nUse /cmds to see all commands.")

    @app.on_message(filters.command("ping"))
    async def ping(_, msg: Message):
        await msg.reply("🏓 Pong!")

    @app.on_message(filters.command("cmds"))
    async def cmds(_, msg: Message):
        await msg.reply("""📜 Available Commands:
/start - Check Bot
/help - Help Menu
/ping - Ping
/setcode - Set FFMPEG Code
/getcode - Current FFMPEG Code
/sysinfo - System Info
/speed - Speedtest
/leech - Download & Compress
/renew - Clear Downloads
/clear - Clear Queue
/logs - Get Logs
/showthumb - Show Thumbnail
/eval - Run Python Code
/bash - Run Bash Command""")
