import random

from discord.ext import commands


class hug(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, ctx, user : str = None):
        if user == None:
            NothingArray = [
                "You hug Nothing",
                "You hug the air",
                "Try hugging a user",
                "How about you hug a user",
                "You hug the air, awesome!",
                "You attempt to hug the oxygen, kewl",
                "Stop hugging the air ffs",
                "Why dont you wanna hug someone?"
            ]
            await ctx.send(random.choice(NothingArray))
            return
        Hug = [
            f"You hug {user}",
            f"You squeeze {user} very tightly ^-^",
            f"You get hugged back!",
            f"You hug {user} wayy too tightly",
            f"You hug me instead",
            f"{user} thanks you for the hug!"
        ]
        await ctx.send(random.choice(Hug))


def setup(bot):
    bot.add_cog(hug(bot))
