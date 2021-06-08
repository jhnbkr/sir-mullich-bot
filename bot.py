from discord.ext import commands

from cogs.events import Events
from cogs.media import Media
from cogs.quote import Quote
from cogs.utility import Utility
from settings import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!")
bot.add_cog(Events(bot))
bot.add_cog(Media(bot))
bot.add_cog(Quote(bot))
bot.add_cog(Utility(bot))

bot.run(DISCORD_TOKEN)
