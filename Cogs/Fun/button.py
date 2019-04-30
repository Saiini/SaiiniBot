from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from discord.ext import commands
import discord
import os
import random
import textwrap
class button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def button(self, ctx, *, txt : str = None):
        if txt == None:
            NothingArray = [
                "Input an argument you tard",
                "Please input something!",
                "no"
            ]
            await ctx.send(random.choice(button))
            return
        width = 8
        image = Image.open('asset/btn.jpg')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('asset/ARIBL0.ttf', 30)
        newtext = textwrap.fill(txt, width)
        draw.text(xy=(89, 224), text=newtext, font=font)
        image.save('asset/btn-new.jpg')
        await ctx.send(file=discord.File(fp='asset/btn-new.jpg'))
        os.remove('asset/btn-new.jpg')
def setup(bot):
    bot.add_cog(button(bot))