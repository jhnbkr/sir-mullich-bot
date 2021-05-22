from discord.ext import commands

from cogs.media import Media
from cogs.quote import Quote
from cogs.utility import Utility
from settings import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!")
bot.add_cog(Media())
bot.add_cog(Quote())
bot.add_cog(Utility())

bot.run(DISCORD_TOKEN)
