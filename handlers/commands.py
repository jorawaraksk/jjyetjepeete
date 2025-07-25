from pyrogram import filters
from pyrogram.types import Message
import subprocess

def init(app):
    @app.on_message(filters.command("bash"))
    async def bash(_, msg: Message):
        cmd = msg.text.split(maxsplit=1)[-1]
        result = subprocess.getoutput(cmd)
        await msg.reply(f"```{result}```")

    @app.on_message(filters.command("eval"))
    async def eval_cmd(_, msg: Message):
        try:
            result = eval(msg.text.split(maxsplit=1)[-1])
            await msg.reply(str(result))
        except Exception as e:
            await msg.reply(str(e))
