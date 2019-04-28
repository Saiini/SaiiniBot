import discord
from discord.ext import commands
from requests import get
import random
import requests
import time
import os
class curl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def curl(self, ctx, url : str = None):
        if url == None:
            NothingArray = [
                "You attempt to get nothing... here is the source: ***absolutely nothing lmao***",
                "You try to send a request to air, sadly their servers are down ;(",
                "curl --data fuckingNothing                         - RECEIVED: NOTHING         JSON: ABSOLUTLEY_NOTHING",
                "try to put a url in you moron",
            ]
            await ctx.send(random.choice(NothingArray))
            return
        req = requests.get(url).content
        await ctx.send("Please wait...")
        time.sleep(3)
        await ctx.send(f"```html\n{req}+\b```")
def setup(bot):
    bot.add_cog(curl(bot))