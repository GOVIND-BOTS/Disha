from AarohiX import app
from pyrogram import Client, filters
 
 
 # The Command to promote a user to admin rights
 @app.on_message(filters.command(["promote", "admin" ], prefixes=["/", "@", "#"]))
 def promote(client, message):
     chat_id = message.chat.id
     from_user = message.from_user
 
     if message.reply_to_message:  # Reply to a message to promote that user
         user_to_promote = message.reply_to_message.from_user
     else:
         message.reply_text("Reply to a user's message to promote them.")
         return
 
     client.promote_chat_member(
         chat_id,
         user_to_promote.id,
         can_change_info=True,
         can_post_messages=True,
         can_edit_messages=True,
         can_delete_messages=True,
         can_invite_users=True,
         can_restrict_members=True,
         can_pin_messages=True,
         can_promote_members=True,
         can_manage_voice_chats=True
     )
     
     message.reply_text(f"Promoted {user_to_promote.mention} to admin.")
 
 # The Command to demote a user from admin rights
 @app.on_message(filters.command("demote") & filters.group)
 def demote(client, message):
     chat_id = message.chat.id
     from_user = message.from_user
 
     if message.reply_to_message:  # Reply to a message to demote that user
         user_to_demote = message.reply_to_message.from_user
     else:
         message.reply_text("Reply to a user's message to demote them.")
         return
     
     client.promote_chat_member(
         chat_id,
         user_to_demote.id,
