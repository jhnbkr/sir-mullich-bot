from cogs import Cog
from constants import USER_MOORE
from utils.message import message_contains_mention, message_contains_text


class Events(Cog):
    @staticmethod
    def contains_moore(message):
        if message_contains_text(message, "moore"):
            return True

        if message_contains_mention(message, USER_MOORE):
            return True

        return False

    @Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if self.contains_moore(message):
            await message.channel.send("*fart*")
