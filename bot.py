import http
import json
import os
import random

import numpy as np

from discord.ext import commands
from dotenv import load_dotenv

from utils import get_random_gif

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


@bot.command()
async def insult(ctx):
    connection = http.client.HTTPSConnection("insult.mattbas.org")
    connection.request("GET", "/api/insult")
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    await ctx.send(data)


@bot.command()
async def compliment(ctx):
    connection = http.client.HTTPSConnection("complimentr.com")
    connection.request("GET", "/api")
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    result = data.get("compliment").capitalize()
    if not result.endswith((".", "!", "?")):
        result += "."
    await ctx.send(result)


@bot.command()
async def chucknorris(ctx):
    connection = http.client.HTTPSConnection("api.chucknorris.io")
    connection.request("GET", "/jokes/random")
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    await ctx.send(data.get("value"))


@bot.command()
async def trump(ctx):
    connection = http.client.HTTPSConnection("tronalddump.io")
    connection.request("GET", "/random/quote", headers={"Accept": "*/*"})
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    await ctx.send(data.get("value"))


@bot.command()
async def advice(ctx):
    connection = http.client.HTTPSConnection("api.adviceslip.com")
    connection.request("GET", "/advice")
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    slip = data.get("slip")
    await ctx.send(slip.get("advice"))


@bot.command()
async def taco(ctx):
    connection = http.client.HTTPSConnection("taco-randomizer.herokuapp.com")
    connection.request("GET", "/random/?full-taco=true")
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    await ctx.send(data.get("recipe"))


@bot.command()
async def joke(ctx):
    connection = http.client.HTTPSConnection("icanhazdadjoke.com")
    connection.request("GET", "/", headers={"Accept": "application/json"})
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    await ctx.send(data.get("joke"))


@bot.command()
async def math(ctx):
    connection = http.client.HTTPConnection("numbersapi.com")
    connection.request("GET", "/random/trivia")
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    await ctx.send(data)


@bot.command()
async def piersblowsdonkeysinhissparetime(ctx):
    await ctx.send(get_random_gif("mrbean"))


@bot.command()
async def moore(ctx):
    await ctx.send(get_random_gif("jesus"))


@bot.command()
async def fart(ctx):
    await ctx.send("*toot*")


@bot.command()
async def cincinnatibowtie(ctx):
    await ctx.send("https://johnbaker.s3.amazonaws.com/images/moore.jpg")


bot.run(TOKEN)
