import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "26934275"
API_HASH = "bcf678e0b1a4ffd5f8e6d11f389fd428"

# Get your token from BotFather on Telegram.
BOT_TOKEN = "6671586333:AAGyjGsFaYRtKWvv5gTwmD3V8SBHGwJx29E"
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Its_me_risanth")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","Sweetyxmusic_robot")
# --------------------------------------------------------
BOT_NAME = getenv("⌜ꜱᴡᴇᴇᴛy ✘ ᴍᴜsɪᴄ 🕊⃝‌⌟" )
# ---------------------------13569561------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://ftyvfbgubhu7:hDZwwlNzlKBzls84ameliamusicbot.f7dzw.mongodb.net/?retryWrites=true&w=majority&appName=AmeliaMusicbot"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "17000000000"))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002475141094"))

# Get this value from PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "854691181" ))


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/risanth96-git/rip-music-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/team_music_association")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/TMK_MUSICSUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 555))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 =("BQFoY5UAhm5GJxAqkfMHqdUFBe9GutHBOaeLPR6IROpQuMVrcAR2KFzFFjIt-QOUaf_uQid4T02MGSDFGEvISxbKkwSghU6pJqXB7BQ14Qb97V1PEySIeTLBc7sAntK29VexSC-sXOkdHWQ2v_5xapWPP3tI62clfiWCOjy9RYLW4UZBZ1FCDqnrEb6xyKP1cxE598ho7tLmKnWc0HRPXEWqpzlbZHKc5pK8bSESnIJSAkXpFHQD9mbFkj3EZ4RJocYdXpvIU9COJlG6bJhzqRXd5OAuvke8yCyYMa1JMbldu-Ah6maUe8gGiFtagVHxV4Cenik6bcgsfGyW5-QnjYktGdNmDQAAAAF3M7q6AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/3d010ee2c59464f6c6705.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/efbf0fedf841bf3f5c953.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/68120737e37cae7520c7b.jpg"
STATS_IMG_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"




def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
