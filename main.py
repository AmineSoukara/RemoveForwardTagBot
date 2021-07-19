# Copyright (C) @Damien - All Rights Reserved
# https://github.com/AmineSoukara/RemoveForwardTagBot/blob/main/LICENSE
# Written by Amine Soukara <AmineSoukara@gmail.com>, June 2021

import os
import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Alty = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


ALTY_CHANNEL = int(os.environ.get("ALTY_CHANNEL", "-1001356154993"))

START_TXT = """
Hello {}, I'm Alive.

Made By @AmineSoukara
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/AmineSoukara/RemoveForwardTagBot'),
        ]]
    )


@Alty.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Alty.on_message(filters.chat(ALTY_CHANNEL) & filters.forwarded)
async def fwdrmv(c, m):

    txt = m.caption
    cp = re.sub("@\\S+", "", txt)
    await m.copy(
        m.chat.id,
        caption=cp + " @DezAlty",
    )
    await m.delete()

@Alty.on_message(filters.chat(ALTY_CHANNEL) & filters.audio)
async def editcap(c, m):

    await c.edit_message_caption(
        chat_id = m.chat.id,
        message_id = m.message_id,
        caption = "@DezAlty", 
        ) 

@Alty.on_message(filters.chat(ALTY_CHANNEL) & filters.photo & filters.caption)
async def editcappic(c, m):
    cap = m.caption
    await c.edit_message_caption(
        chat_id = m.chat.id,
        message_id = m.message_id,
        caption = cap + "\n@DezAlty", 
        ) 


Alty.run()
