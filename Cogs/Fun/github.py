import requests
import discord
from discord.ext import commands
class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context = True, alias = ["ghub", "gh", "gitH"])
    async def github(self, ctx, search : str = None):
        if search == None:
            await ctx.send("You must specify a Github user Or Repository to search!")
            return
        await ctx.send("https://github.com/"+search)
def setup(bot):
    bot.add_cog(github(bot))