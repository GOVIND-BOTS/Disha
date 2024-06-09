import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app

from pyrogram.types import Message
from datetime import datetime
from time import time
from pyrogram.errors import MessageDeleteForbidden, RPCError
from asyncio import sleep
from pyrogram import Client, enums
from pyrogram.types import Message, User
from pyrogram import Client, enums, filters

# Commands list
CMDS = [
    "guddu", "hii", "hello", "bot", "abhi", "kider", "vc", "ok", "lol", "haa", "nahi", "yes", "sure", "@govind_official_mppp",
    "trisha", "@Deep151pk", "kumar", "op", "don", "govind", "@goldy", "Please", "you", "Byy", "yrr", "bro", "bhai", "chat",
    "Morning", "after", "noon", "night", "me", "noi", "nahi", "sir", "join", "superban", "music", "song", "team", "proof",
    "reason", "bhkk", "ider", "se", "Why", "Personal", "online", "offline", "welcome", "ek", "name", "hu"
]

# Reaction list
REACTIONS = [
    '👍', '❤️', '🔥', '🥰', '👏', '😁', '🤩', '👌', '🥱', '😍', '❤️‍🔥', '💯', '🤣', '⚡️', '😴', '👀', '🙈', '🤝',
    '🤗', '🤪', '💘', '😘', '😎'
]

@app.on_message(filters.command(CMDS, prefixes=[""]))
async def handle_incoming_messages(client, message: Message):
    reaction = random.choice(REACTIONS)
    success = await react_to_message(client, message, reaction)
    if not success:
        print("All positive reactions failed.")

async def react_to_message(client, message: Message, reaction: str):
    try:
        if hasattr(message, 'id'):
            await client.send_reaction(message.chat.id, message.id, reaction)
            return True
        else:
            print("Message object does not have id attribute.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
