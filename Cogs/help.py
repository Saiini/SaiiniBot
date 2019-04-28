from discord.ext import commands
import discord
from datetime import datetime
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self, ctx):

        await ctx.send()
def setup(bot):
    bot.add_cog(help(bot))