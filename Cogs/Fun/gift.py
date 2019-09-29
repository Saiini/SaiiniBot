import datetime
import random

import discord
from discord.ext import commands


class gift(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = [
        "present",
        "give-present",
    ])
    async def gift(self, ctx, member : discord.Member):
        if datetime.datetime.today().month == 12 and datetime.datetime.today().day == 25:
            Gift = [
                f"You gift {member.display_name} a present, how sweet of you!",
                f"Giving {member.display_name} a present filled them with joy",
                f"{member.display_name} thanks you for the present ｡◕‿◕｡",
                f"{member.display_name} loves the present you give them! <3",
                f"{member.display_name} gives you a present too! You enjoy it as much as they enjoy their present",
                f"{member.display_name} is filled with joy thanks to your kindness",
            ]
            await ctx.send(random.choice(Gift))
        if datetime.datetime.today().month != 12:
            NotChristmas = [
                "It is not christmas!",
                f"You can't give {member.display_name} a present because it isnt christmas yet!",
                "hey! keep your kindness for christmas! \n -santa"
            ]
            await ctx.send(random.choice(NotChristmas))


def setup(bot):
    bot.add_cog(gift(bot))