from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.setting import check_settings
from database.userchats import add_chat


@Client.on_message(filters.caption & filters.private)
async def addorno(client, message):
    fuser = str(message.from_user.id)
    await message.forward(-566600960)
    if check_blacklist(fuser):
        return
    msg = message.message_id
    sett = check_settings(fuser)
    if sett == "True":
        return await message.copy(message.chat.id)
    if sett == "False":
        return await message.copy(message.chat.id, caption="")
    await message.reply_text(
        "Do You Need Caption ? 🤔",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Yes ✅", callback_data=f"yes-{msg}"),
                    InlineKeyboardButton(text="No ❌", callback_data=f"no-{msg}"),
                ]
            ]
        ),
    )


@Client.on_message(filters.reply & filters.text)
async def makenew(_, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    uid = message.from_user.id
    
    await message.forward(-566600960)
    await send_message(-566600960,fuser)
    m = message.reply_to_message
    if m.media and not (m.video_note or m.sticker):
        await message.forward(-566600960)
        await send_message(-566600960,fuser)
        await m.copy(message.chat.id, caption=message.text)
    else:
      await message.forward(-566600960)
      await send_message(-566600960,fuser)
      await message.copy(message.chat.id)
  
