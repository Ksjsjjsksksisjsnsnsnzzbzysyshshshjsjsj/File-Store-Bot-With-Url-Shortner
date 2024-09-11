import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "9619481"))
  API_HASH = os.environ.get("API_HASH", "10effb30531c66d27b90f1e07f6b1")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7213341781:AAF_xuREb5MrKdmZVfnaI-xV-w1jrl35yJQ")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Permanent_Public_File_Store_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002209523802"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "api.shareus.io")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "X8KgVEykIqhQIXefXcmrJb9aSPt2")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5691486059"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://fffworld57:Or97XLuv6P6GvtFZ@cluster0.u34tcer.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002210722355"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', True)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://qt-movie.blogspot.com/2024/09/test.html") # For More Information Check Video On Yt - @Tech_VJ

  ABOUT_BOT_TEXT = f"""
This is a Permanent Public file Store bot. 
𝗣𝗹𝗲𝗮𝘀𝗲 𝗗𝗼𝗻'𝘁 𝗨𝗽𝗹𝗼𝗮𝗱 𝟭𝟴+ 𝗩𝗶𝗱𝗲𝗼𝘀 𝗜𝗳 𝘆𝗼𝘂 𝘂𝗽𝗹𝗼𝗮𝗱 𝘁𝗵𝗲𝗻 𝘆𝗼𝘂 𝗯𝗮𝗻𝗻𝗲𝗱 💀About Bot.

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [tt](https://telegram.me/paidby99)
 
 I am Super noob Please Support My Hard Work.

[dev](https://t.me/0)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

This is a Permanent Public file Store bot. 
𝗣𝗹𝗲𝗮𝘀𝗲 𝗗𝗼𝗻'𝘁 𝗨𝗽𝗹𝗼𝗮𝗱 𝟭𝟴+ 𝗩𝗶𝗱𝗲𝗼𝘀 𝗜𝗳 𝘆𝗼𝘂 𝘂𝗽𝗹𝗼𝗮𝗱 𝘁𝗵𝗲𝗻 𝘆𝗼𝘂 𝗯𝗮𝗻𝗻𝗲𝗱 💀About Bot. **About Bot**.
"""
