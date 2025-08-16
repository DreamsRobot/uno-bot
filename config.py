# config.py

import os

# Get bot token from environment variable (safer for deployment)
BOT_TOKEN = os.getenv("BOT_TOKEN", "PUT-YOUR-BOT-TOKEN-HERE")

# Optional: Owner/Admin IDs
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# MongoDB / Database URI (if the bot uses DB)
MONGO_URI = os.getenv("MONGO_URI", "")

# Other settings
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
