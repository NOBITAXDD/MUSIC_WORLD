import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/088e7be378ea5a5fc2854.jpg",
        caption=f"""**๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐
สแดแด สแดษดแดสแด สส [๐๐๐๐๐๐_๐๐](https://t.me/Nobi_xxd)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " [๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ] ", url=f"https://t.me/AAPLI_YAARI")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "hi", "NOBITA_XD"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/088e7be378ea5a5fc2854.jpg",
        caption=f"""HELLO ๐ค""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " [๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ] ", url=f"https://t.me/AAPLI_YAARI")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/088e7be378ea5a5fc2854.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " [๐๐๐ฅ๐ค๐จ๐๐ฉ๐ค๐ง๐ฎ] ", url=f"https://t.me/Nobi_xxd")
                ]
            ]
        ),
    )
