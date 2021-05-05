from discord.ext import commands

from utils.http import HTTPClient


class Quote(commands.Cog):
    @commands.command(help="Chuck Norris counted to infinity... twice.")
    async def chucknorris(self, ctx):
        client = HTTPClient()
        response = client.get("https://api.chucknorris.io/jokes/random")
        await ctx.send(response.get("value"))

    @commands.command(help="Bad")
    async def compliment(self, ctx):
        client = HTTPClient()
        response = client.get("https://complimentr.com/api")
        compliment = response.get("compliment").capitalize()
        if not compliment.endswith((".", "!", "?")):
            compliment += "."
        await ctx.send(compliment)

    @commands.command(help="Good")
    async def insult(self, ctx):
        client = HTTPClient()
        response = client.get("https://insult.mattbas.org/api/insult")
        await ctx.send(response)

    @commands.command(help="LOL")
    async def joke(self, ctx):
        client = HTTPClient()
        response = client.get(
            "https://icanhazdadjoke.com", headers={"Accept": "application/json"}
        )
        await ctx.send(response.get("joke"))
