import os
from discord.ext import commands
import random
class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx, ip : str = None):
        if ip == None:
            NothingArray = [
                "Pinging nothing... SERVER IS UP!",
                "Please provide something for me to ping",
                "Pinging oxygen... SERVER IS UP!"
            ]
            await ctx.send(random.choice(NothingArray))
            return
        await ctx.send("Please wait...")
        response = os.system("ping "+ip)
        if response == 0:
            await ctx.send("***Pinged server is Online!***")
        else:
            await ctx.send("***Request timed out.***")
def setup(bot):
    bot.add_cog(ping(bot))