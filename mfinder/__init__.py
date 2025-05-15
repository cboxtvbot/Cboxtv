import os
import re
import logging
import logging.config
from dotenv import load_dotenv


load_dotenv()


id_pattern = re.compile(r"^.\d+$")

# vars
APP_ID = os.environ.get("APP_ID", "28862799")
API_HASH = os.environ.get("API_HASH", "3dc3be3bfb934a68aa280044b064ccee")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8074681333:AAHNHcNbU0nr3epf0fti_AHH36nfzSXxSqU")
DB_URL = os.environ.get("DB_URL", " mongodb+srv://cboxtvbot:Qwerty123%@cluster0.pjhktae.mongodb.net/")
OWNER_ID = int(os.environ.get("OWNER_ID", "7886433884"))
ADMINS = [
    int(user) if id_pattern.search(user) else user
    for user in os.environ.get("ADMINS", "7886433884").split()
] + [OWNER_ID]
DB_CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in os.environ.get("DB_CHANNELS", "-1002543001708").split()
]

try:
    import const
except Exception:
    import sample_const as const

START_MSG = const. welcome
START_KB = const.welcome
HELP_MSG = const.welcome
HELP_KB = const.welcome


# logging Conf
logging.config.fileConfig(fname="config.ini", disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
