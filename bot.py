import os
from config import *
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client, filters
from pyrogram.types import Message
import logging

app = Client(
    "Team Epic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("webss"))
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "Give A Url To Fetch Screenshot."
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("No Such Website.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))

print("hellow world")
app.run()
