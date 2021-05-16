from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
Hi, I am **ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!

You Can too Clone me :-
https://github.com/ProThinkerGang/Anonymous-Bot
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Caption Setting", callback_data="captz")],
        [InlineKeyboardButton("Support Group", url="t.me/FutureCodes")],
    ]
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    NewVar = START
    ba ='India 🇮🇳 '
    if var.OWNER_ID and not message.from_user.id == var.OWNER_ID:
        geto = await client.get_users(var.OWNER_ID)
        NewVar += f"\n\nMaintained By 🇮🇳 with <3"
    else:
        NewVar += "\n\n**Onwer Commands** - https://telegra.ph/Owner-Commands-05-13"
    await message.reply_text(
        NewVar, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )
