import os
import re
import asyncio
from AarohiX import app
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from random import choice
from ..logging import LOGGER
from AarohiX.config import API_ID, API_HASH

IMG = ["https://telegra.ph/file/cefd3211a5acdcd332415.jpg", "https://telegra.ph/file/30d743cea510c563af6e3.jpg", "https://telegra.ph/file/f7ae22a1491f530c05279.jpg", "https://telegra.ph/file/2f1c9c98452ae9a958f7d.jpg"]

MESSAGE = "Heya! I'm a music bot hoster/Cloner\n\nI can Host Your Bot On My Server within seconds\n\nTry /clone Token from @botfather"

@app.on_message(filters.private & filters.command("start"))
async def hello(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/onlin_love_filings"),
        ],
        [
            InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/govind_official_mpp"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{choice(IMG)}", caption=MESSAGE, reply_markup=reply_markup)

@app.on_message(filters.private & filters.command("clone"))
async def clone(client: Client, message: Message):
    chat = message.chat
    text = await message.reply("Usage:\n\n /clone token")
    cmd = message.command
    phone = message.command[1]
    try:
        await text.edit("Booting Your Client")
        # change this Directory according to your repo
        cloned_client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "AarohiX.modules"})
        await cloned_client.start()
        user = await cloned_client.get_me()
        await message.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @{ASSUSERNAME} To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await message.reply(f"ERROR: {str(e)}\nPress /start to Start again.")
