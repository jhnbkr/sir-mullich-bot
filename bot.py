import os
import random
import numpy as np

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="sir ")


@bot.command()
async def team(ctx, teams_count: int, *names: str):
    names = list(names)
    random.shuffle(names)
    teams = list(np.array_split(names, teams_count))
    for c, t in enumerate(teams):
        await ctx.send(f"Team {c + 1}: {', '.join(t)}")


bot.run(TOKEN)
