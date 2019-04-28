import discord
from discord.ext import commands
import random
class ban(commands.Command):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions()
    async def ban(self, ctx, member : str = None, reason : str = None):
        if member == None:
            NothingArray = [
                "You try to ban **Nothing**",
                "Banning nothing was ineffective!",
                "You ban **Nothing** for **No reason**, You cruel human being...",
                "You attempt to ban the air... Now we can't breath... Thanks alot wise-guy",
                "The Air: Oniichan please dont ban me UwU",
                "Arghhh seargeant... im tryna ban nothing but im **DUMMY THICC**"
                ]
            await ctx.send(random.choice(NothingArray))
            return

def setup(bot):
    bot.add_cog(bot(ban))