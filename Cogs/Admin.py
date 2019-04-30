from discord.ext import commands
import discord
import random
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{ctx.author.mention} has banned {member.display_name}. \nHere is the Members ID:```yml\n{member.id}```")
        except:
            return
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason : str = None):
        try:

            await member.kick(reason=reason)
            await ctx.send(f"{ctx.author.mention} has kicked {member.display_name}.\n Reason: **{reason}**")
        except:
            return
def setup(bot):
    bot.add_cog(Admin(bot))