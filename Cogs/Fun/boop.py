import discord
from discord.ext import commands
import random
class boop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def boop(self, ctx, *, member : str = None):
        if member == None:
            NothingArray = [
                "You attempt to boop no ones nose... turns out... it was ineffective...",
                "You can't boop nothing silly!",
                "Try booping something Fun than air...",
                "How about booping someone?"
            ]
            await ctx.send(random.choice(NothingArray))
            return
        Boop = [
            f"You boop {member}!",
            f"booop! {member}",
            f"You boop {member}'s nose ^-^",
            f"You get booped back, ***AGGRESSIVELY***",
            f"You boop {member}'s nose till they get tired of it ^-^",
        ]
        await ctx.send(random.choice(Boop))
def setup(bot):
    bot.add_cog(boop(bot))