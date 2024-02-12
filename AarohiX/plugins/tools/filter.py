import asyncio
import re
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton

from AarohiX import mongo

edit_time = 5

file1 = "https://telegra.ph/file/9a85d0a873e2dd80d278d.jpg"
file2 = "https://telegra.ph/file/9e7815284031452afa9e5.jpg"
file3 = "https://telegra.ph/file/dcc5e003287f69acea368.jpg"
file4 = "https://telegra.ph/file/ed1ce7fee94f46b0f671e.jpg"
file5 = "https://telegra.ph/file/701028ce085ecfa961a36.jpg"

BOT_NAME = "YourBotName"  # Replace with your actual bot name

app = Client("my_bot")


@app.on_message(filters.command("myinfo"))
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.from_user.first_name
    button = [[InlineKeyboardButton("ɪɴғᴏʀᴍᴀᴛɪᴏɴ", callback_data="informations")]]
    on = await event.reply_photo(
        photo=file2,
        caption=f"ʜᴇʏ {firstname}, \nᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ \n ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ʏᴏᴜ",
        reply_markup=InlineKeyboardMarkup(buttons=button),
    )

    await asyncio.sleep(edit_time)
    ok = await on.edit_media(media=InputMediaPhoto(file3), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok2 = await ok.edit_media(media=InputMediaPhoto(file5), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok3 = await ok2.edit_media(media=InputMediaPhoto(file1), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok4 = await ok3.edit_media(media=InputMediaPhoto(file4), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok5 = await ok4.edit_media(media=InputMediaPhoto(file2), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok6 = await ok5.edit_media(media=InputMediaPhoto(file1), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok7 = await ok6.edit_media(media=InputMediaPhoto(file3), reply_markup=InlineKeyboardMarkup(buttons=button))

    await asyncio.sleep(edit_time)
    ok8 = await ok7.edit_media(media=InputMediaPhoto(file5), reply_markup=InlineKeyboardMarkup(buttons=button))


@app.on_callback_query(filters.regex("information"))
async def callback_query_handler(event):
    try:
        boy = event.from_user.id
        PRO = await app.get_users(boy)
        LILIE = f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME}\n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ: {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ: {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜʀ ʙᴏᴛ : {PRO.is_bot} \n"
        LILIE += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.is_restricted} \n"
        LILIE += f"ᴜsᴇʀ ɪᴅ: {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : @{PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")
