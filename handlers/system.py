from pyrogram import filters
from pyrogram.types import Message
from utils.sysinfo import get_system_info
from utils.speedtest import run_speedtest

def init(app):
    @app.on_message(filters.command("sysinfo"))
    async def sysinfo(_, msg: Message):
        await msg.reply(get_system_info())

    @app.on_message(filters.command("speed"))
    async def speed(_, msg: Message):
        await msg.reply(run_speedtest())
