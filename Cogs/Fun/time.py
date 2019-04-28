import discord
from discord.ext import commands
import datetime
import pytz
class time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(alias = ["bot-time"])
    async def time(self, ctx):
        now = datetime.datetime.now()
        dt_pacific = now.astimezone(pytz.timezone('US/Pacific'))
        embed = discord.Embed(title = "My current time is...", description=dt_pacific.strftime("%H:%M %p\n%m/%d/%Y"), color=discord.Color.green())
        await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(time(bot))
