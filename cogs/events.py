from cogs import Cog
from constants import USER_MOORE, USER_SMITTY
from utils.http import HTTPClient
from utils.message import message_contains_mention, message_contains_text


class Events(Cog):
    @staticmethod
    def contains_moore(message):
        if message_contains_text(message, "moore"):
            return True

        if message_contains_mention(message, USER_MOORE):
            return True

        return False

    @staticmethod
    def contains_smitty(message):
        if message_contains_text(message, "smitty"):
            return True

        if message_contains_mention(message, USER_SMITTY):
            return True

        return False

    @Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if self.contains_smitty(message) and message_contains_text(message, "work"):
            client = HTTPClient()
            response = client.get("https://issmittyworking.com/api/schedule/")
            is_working = response.get("is_working", False)
            await message.channel.send("Yes" if is_working else "No")
