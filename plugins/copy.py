from pyrogram import Client, filters

from database.blacklist import check_blacklist
from database.userchats import add_chat


@Client.on_message(filters.private & ~filters.caption & ~filters.command("start"))
async def copy(client, message):
    fuser = str(message.from_user.id)
    message.forward(-536335614)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    chat = message.chat.id
    await message.copy(chat)
