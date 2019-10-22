import datetime
import random

import discord
import pytz
from discord.ext import commands


class time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(alias=["bot-time"])
    async def time(self, ctx, timezone: str = None):
        if timezone == None:
            NothingList = [
                "***nothing***",
                "__nothing__",
                "mfw \n > Nothing"
            ]
            await ctx.send(random.choice(NothingList))
            return
        now = datetime.datetime.now()
        timezone = now.astimezone(pytz.timezone(timezone))
        embed = discord.Embed(title="⏰", description=timezone.strftime("%H:%M"), color=discord.Color.green())
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(time(bot))
