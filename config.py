import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "20028561"
API_HASH = "0f3793daaf4d3905e55b0e44d8719cad"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7189150788:AAHZGD_aXoqk1MhQUV3hbPKEansWZiFiH2c"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://darkth0ughtss00:loniko0908@music.njvuzcz.mongodb.net/?retryWrites=true&w=majority&appName=Music"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002069412308


# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = "5630057244"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = ""
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = "HRKU-ed430d84-df33-4933-a335-a441675650ce"

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Darkth0ughtss/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("https://t.me/DominosXd", "https://t.me/DominosXd")
SUPPORT_CHAT = getenv("https://t.me/DominosXd", "https://t.me/DominosXd")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = "ea5056b8de21435296daa3ca6a9b1240"
SPOTIFY_CLIENT_SECRET = "e5071dc9dee54dfa94805c949cbc230f"


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = 3221225472
TG_VIDEO_FILESIZE_LIMIT = 3221225472
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQExnJEAa7TxoJjfia_UkfbFkMs6qTCmYV563TgzZ-lH1lHiTo8fLoY-9rFNIpA9iORciDLry8877tz6sm90AdN1EoTNrWOH-eMEIMNHBg2ToE4yN0HA_1VAZ0UKAEZyhdS8v3ZFRpeWqttqS8up55Pu9Q83UVX4_9_vIPPbCUofhCpEiUtj7whAWT0xhmfWeHvSd82KjmvXVUMAddW832k0lrHTnPvNOsWmekNTCv2tjKcMgt_mZREpq0zTD98cNePUVs8LR1cpzKVJQhOskAfgXy0AOhFKEojm7qOx3a9_7H0n3q9HMwR-7HpoLCuyhI4azgkS1lYGP90ocSQLxnkvYzMMYAAAAAGP-OJsAA"
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
    "START_IMG_URL", "https://telegra.ph/file/d54925cd5c0f1a60fcac5.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
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
