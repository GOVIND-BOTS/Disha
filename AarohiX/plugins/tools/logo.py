from pyrogram import Client, filters
from pyrogram.types import Message
import requests



@app.on_message(filters.command("logo"))
async def logo_command(client, message: Message):
    if len(message.command) == 1:
        return await message.reply_text("Usage:\n\n /logo govind")

    logo_name = message.text.split(" ", 1)[1]
    api_url = f"https://api.sdbots.tech/logohq?text={logo_name}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        await message.reply_photo(photo=response.url)

@app.on_message(filters.command("animelogo"))
async def animelogo_command(client, message: Message):
    if len(message.command) == 1:
        return await message.reply_text("Usage:\n\n /animelogo govind")

    logo_name = message.text.split(" ", 1)[1]
    api_url = f"https://api.sdbots.tech/anime-logo?name={logo_name}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        await message.reply_photo(photo=response.url)
