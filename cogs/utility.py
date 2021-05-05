import random

import numpy as np
from discord.ext import commands

import settings


class Utility(commands.Cog):
    @commands.command(help="Make a random choice")
    async def choose(self, ctx, *choices: str):
        await ctx.send(random.choice(choices))

    @commands.command(help="70/30 odds")
    async def flip(self, ctx):
        await ctx.send("Heads" if bool(random.getrandbits(1)) else "Tails")

    @commands.command(help="Spam @Smitty")
    async def repeat(self, ctx, count: int, *args: str):
        count = max(1, min(count, settings.REPEAT_LIMIT))
        for i in range(count):
            await ctx.send(" ".join(args))

    @commands.command(help="Roll dice {COUNT}d{SIDES} (e.g. 2d6)")
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.lower().split("d"))
        except ValueError:
            await ctx.send("Format has to be in NdN!")
            return

        await ctx.send(", ".join(str(random.randint(1, limit)) for r in range(rolls)))

    @commands.command(help="Shuffle list of choices")
    async def shuffle(self, ctx, *choices: str):
        choices = [*choices]
        random.shuffle(choices)
        await ctx.send(", ".join(choices))

    @commands.command(help="Random team assignment")
    async def team(self, ctx, count: int, *names: str):
        names = list(names)
        random.shuffle(names)
        teams = list(np.array_split(names, count))
        for c, t in enumerate(teams):
            await ctx.send(f"Team {c + 1}: {', '.join(t)}")
