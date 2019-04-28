from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ext import commands
import discord
import os
import textwrap
class clippy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def clippy(self, ctx, *, text : str = None):
        if text == None:
            return
        width = 40.2
        newtext = textwrap.fill(text, width)
        image = Image.open('asset/clippy.jpg')
        font = ImageFont.truetype('asset/clippy.ttf', 12)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(12, 12), text=newtext, fill='rgb(0,0,0)' ,font=font)
        image.save('asset/clippynew.jpg')
        await ctx.send(file=discord.File(fp='asset/clippynew.jpg'))
        os.remove('asset/clippynew.jpg')
    @commands.command()
    async def clippyoption(self, ctx, *, text : str = None):
        if text == None:
            return
        width = 20
        if len(text) > 100:
            await ctx.send("Please provide something over 100 chars!")
            return
        newtext = textwrap.fill(text, width)
        image = Image.open('asset/clippy_option.jpg')
        font = ImageFont.truetype('asset/clippy.ttf', 40)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(46, 49), text=newtext, fill='rgb(0,0,0)', font=font)
        image.save('asset/clippyoptionnew.jpg')
        await ctx.send(file=discord.File(fp='asset/clippyoptionnew.jpg'))
        os.remove('asset/clippyoptionnew.jpg')
def setup(bot):
    bot.add_cog(clippy(bot))
