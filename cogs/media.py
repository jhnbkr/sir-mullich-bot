from discord.ext import commands

import settings
from cogs import Cog
from utils.http import HTTPClient


class GiphyClient(HTTPClient):
    @property
    def base_url(self):
        return "https://api.giphy.com"

    @property
    def auth_params(self):
        return {"api_key": settings.GIPHY_API_KEY}

    def build_params(self, **params):
        return {**self.auth_params, **params}


class Media(Cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.giphy = GiphyClient()

    def get_gif(self, id):
        response = self.giphy.get(
            f"/v1/gifs/{id}",
            params={**self.giphy.build_params()},
        )
        if isinstance(response, dict):
            return response.get("data").get("url")

    def get_random_gif(self, tag):
        response = self.giphy.get(
            "/v1/gifs/random",
            params={**self.giphy.build_params(tag=tag)},
        )
        if isinstance(response, dict):
            return response.get("data").get("url")

    @commands.command(help="Idiot")
    async def moore(self, ctx):
        await ctx.send("https://johnbaker.s3.amazonaws.com/images/moore.jpg")

    @commands.command(help="NICCCE")
    async def nice(self, ctx):
        await ctx.send(self.get_gif("pCO5tKdP22RC8"))

    @commands.command(help="What next, an ACTUAL slap in the face?")
    async def slap(self, ctx):
        await ctx.send(self.get_random_gif("slap"))

    @commands.command(help="As is tradition")
    async def piersblowsdonkeysinhissparetime(self, ctx):
        await ctx.send(self.get_random_gif("donkey"))

    @commands.command(help="T asked for pizza")
    async def pizza(self, ctx):
        await ctx.send(self.get_random_gif("pizza"))

    @commands.command(help="A refreshing warm Busch")
    async def warmbusch(self, ctx):
        await ctx.send("https://warmbusch.com")

    @commands.command(help="Sir Mullich has his eye on T")
    async def t(self, ctx):
        await ctx.send(self.get_gif("ZKrIYV3oIzIL6"))
