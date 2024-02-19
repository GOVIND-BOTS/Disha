from pyrogram import Client, filters
from AarohiX import app
import config
from config import OWNER_ID

@app.on_message(filters.private & ~filters.me)
async def forward_to_owner(client, message):
    if message.from_user.id != OWNER_ID:6377689548
        await client.forward_messages(chat_id=OWNER_ID, from_chat_id=message.chat.id, message_ids=message.message_id)

@app.on_message(filters.private & filters.user(6377689548) & ~filters.me)
async def forward_to_user(client, message):
   
    replied_to = message.reply_to_message
    if replied_to:
        
        user_message = replied_to.reply_to_message
        if user_message:
            await client.forward_messages(chat_id=user_message.chat.id, from_chat_id=message.chat.id, message_ids=message.message_id)
