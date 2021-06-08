from discord.ext.commands import Cog as BaseCog


class Cog(BaseCog):
    def __init__(self, bot):
        self.bot = bot
