import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "help")
    async def help(self, ctx):
        embed = discord.Embed(title="Fun", description="", color=discord.Color.dark_red())
        embed.add_field(name="boop", value="└─``Boops a user!``", inline=True)
        embed.add_field(name="button", value="└─``Makes a button meme``", inline=True)
        embed.add_field(name="clippy", value="└─``Makes a clippy meme``", inline=True)
        embed.add_field(name="gift", value="└─``Gifts a user on Christmas!``", inline=True)
        embed2 = discord.Embed(title="Moderation", description="", color=discord.Color.dark_red())
        embed2.add_field(name="ban", value="└─``Bans a user``", inline=True)
        embed2.add_field(name="kick", value="└─``Kicks a user``", inline=True)
        await ctx.author.send(embed=embed)
        await ctx.author.send(embed=embed2)


def setup(bot):
    bot.add_cog(help(bot))