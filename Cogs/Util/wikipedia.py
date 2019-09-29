import random
import textwrap

import discord
import wikipedia
from discord.ext import commands


class wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wikipedia(self, ctx, *, query : str = None):
        if query == None:
            NothingArray = [
                "I searched up **Nothing** and **Nothing** Popped up!",
                "Please input something for me to search!",
                "Wikipedia didnt like that!",
                "Wikipedia says: Input something",
                "Wikipedia doesn't like that",
            ]
            await ctx.send(random.choice(NothingArray))
            return
        try:
            search = wikipedia.page(query)
        except wikipedia.DisambiguationError:
            await ctx.send(f"Sorry! it looks like i couldnt find results for: **{query.capitalize()}** on wikipedia! Please make sure the word you input is not an Acronym!")
            return
        shorten = textwrap.wrap(search.content, 500)
        embed = discord.Embed(title="Wikipedia", color=0xCD6735, url=f"https://en.wikipedia.org/wiki/Main_Page")
        embed.add_field(name=f"Search results for **{query.capitalize()}**", value=shorten[0])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(wiki(bot))