from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AmritaXMusic import app
from config import BOT_USERNAME
from AmritaXMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ || @team_music_association ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""


@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝙏𝙚𝙖𝙢 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/TMK_MUSICSUPPORT"),
          InlineKeyboardButton("𝐓ᴇᴀᴍ 𝗩ᴀᴍᴘɪʀᴇ 𝐍ᴇᴛᴡᴏʀᴋ   ","https://t.me/TMK_MUSICSUPPORT"),
          ],
               [
                InlineKeyboardButton("�ᴇᴀᴍ �ᴀᴍᴘɪʀᴇ �ᴇᴛᴡᴏʀᴋ 𝙏𝙚𝙖𝙢", url=f"https://t.me/TMK_MUSICSUPPORT"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/Sweetyxmusic_robot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/5DC.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
