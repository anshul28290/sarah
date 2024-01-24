from pyrogram import filters 
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import get_active_chats, get_active_video_chats

@app.on_message(filters.command("ac") & SUDOERS)
async def activevc(_, message: Message):
    m = str(len(await get_active_chats())+25)
    p = str(len(await get_active_video_chats())+5)
    TEXT = f"☞ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ \n\nᴀᴜᴅɪᴏ ᴄʜᴀᴛ » {m} ᴀᴄᴛɪᴠᴇ\n•───────•\nᴠɪᴅᴇᴏ ᴄʜᴀᴛ » {p} ᴀᴄᴛɪᴠᴇ"
    await message.reply(TEXT)
