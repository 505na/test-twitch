import irc.bot
import random
import os
import sys
import logging

from dotenv import load_dotenv
from commands import process_command

# ==================================
# LOGGING
# ==================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger("TwitchBot")

# ==================================
# ŁADOWANIE .ENV
# ==================================

load_dotenv()

TOKEN = os.getenv("TOKEN")
NICK = os.getenv("NICK")
CHANNEL = os.getenv("CHANNEL")

DISCORD_LINK = "https://discord.gg/VUmbQZZmvM"

# ==================================
# SPRAWDZENIE ENV
# ==================================

if not TOKEN:
    logger.error("Brak TOKEN w .env")
    exit()

if not NICK:
    logger.error("Brak NICK w .env")
    exit()

if not CHANNEL:
    logger.error("Brak CHANNEL w .env")
    exit()

# ==================================
# IGNOROWANI
# ==================================

IGNORED_USERS = {
    "nightbot",
    "streamelements",
    "streamlabs",
    "moobot",
    "botrixofficial",
    "tangiabot",
    "own3d",
    "creatisbot",
    "soundalerts",
    NICK.lower()
}

# ==================================
# BOT
# ==================================

class TwitchBot(irc.bot.SingleServerIRCBot):

    def __init__(self):

        server = "irc.chat.twitch.tv"
        port = 6667

        super().__init__(
            [(server, port, TOKEN)],
            NICK,
            NICK
        )

        self.channel = CHANNEL
        self.chatters = set()
        self.streamer = CHANNEL.strip("#").lower()

    # ==================================
    # LOSOWY CHATTER
    # ==================================

    def get_random_chatter(self, exclude_user=None):

        valid_users = [
            u for u in self.chatters
            if u not in IGNORED_USERS
            and u != exclude_user
        ]

        if not valid_users:
            return None

        return random.choice(valid_users)

    # ==================================
    # POŁĄCZENIE
    # ==================================

    def on_welcome(self, connection, event):

        logger.info(f"Zalogowano jako {NICK}")

        # Request Twitch-specific capabilities for tags
        connection.cap("REQ", ":twitch.tv/tags")

        connection.join(self.channel)

        logger.info(f"Dołączono do {self.channel}")

    # ==================================
    # WIADOMOŚCI
    # ==================================

    def on_pubmsg(self, connection, event):

        try:

            username = event.source.nick.lower()
            message = event.arguments[0]

            logger.info(f"[CHAT] {username}: {message}")

            # zapisuj użytkowników
            if username not in IGNORED_USERS:
                self.chatters.add(username)

            msg = message.strip().lower()

            # Extract tags if available
            tags = {}
            if hasattr(event, 'tags') and event.tags:
                tags = {tag['key']: tag['value'] for tag in event.tags}

            # Przetwórz komendę
            process_command(msg, connection, self.channel, username, self.chatters, IGNORED_USERS, DISCORD_LINK, self.streamer, tags)

        except Exception as e:

            logger.exception(f"Wystąpił błąd: {e}")

# ==================================
# START
# ==================================

logger.info("Uruchamianie bota...")

bot = TwitchBot()
bot.start()