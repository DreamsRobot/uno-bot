# config.py
import os

API_ID = int(os.getenv("API_ID", "123456"))       # From my.telegram.org
API_HASH = os.getenv("API_HASH", "your_api_hash") # From my.telegram.org
BOT_TOKEN = os.getenv("BOT_TOKEN", "PUT-YOUR-BOT-TOKEN-HERE")

OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))
MONGO_URI = os.getenv("MONGO_URI", "")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
