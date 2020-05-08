import os
import random

import numpy as np
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command()
async def team(ctx, teams_count: int, *names: str):
    names = list(names)
    random.shuffle(names)
    teams = list(np.array_split(names, teams_count))
    for c, t in enumerate(teams):
        await ctx.send(f"Team {c + 1}: {', '.join(t)}")


@bot.command()
async def flip(ctx):
    await ctx.send("Heads" if bool(random.getrandbits(1)) else "Tails")


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split("d"))
    except ValueError:
        await ctx.send("Format has to be in NdN!")
        return

    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


bot.run(TOKEN)
