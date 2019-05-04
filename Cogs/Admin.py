from discord.ext import commands
import discord
import random
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
        if commands.BotMissingPermissions:
            await ctx.send("It appears you havent assigned me valid permissions to run this command! Sorry!")
            return
        if commands.MissingPermissions:
            await ctx.send("You do not have permission to run this command. Apologies!")
            return
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f"Banned user: {member.display_name}", description=f"Reason: {reason}", color=discord.Color.red())
            await ctx.send(embed=embed)
        except:
            return
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason : str = None):
        if commands.BotMissingPermissions:
            await ctx.send("It appears you havent assigned me valid permissions to run this command! Sorry!")
            return
        if commands.MissingPermissions:
            await ctx.send("You do not have permission to run this command. Apologies!")
            return
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(title=f"Kicked user: {member.display_name}", description=f"Reason: {reason}", color=discord.Color.darker_grey())
            await ctx.send(embed=embed)
        except:
            return
    '''
    @commands.command()
    @commands.has_permissions(kick_mebers = True)
    async def
    '''
def setup(bot):
    bot.add_cog(Admin(bot))