from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ext import commands
import discord
import os
import textwrap
import random
class clippy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def clippy(self, ctx, *, text : str = None):
        if text == None:
            NothingArray = [
                "Clippy says: *Please provide some text!*",
                "Clippy says: *Input some arguments!*",
                "Input some text for clippy!",
                "Please provide text for clippy!"
            ]
            await ctx.send(random.choice(NothingArray))
            return
        width = 40
        newtext = textwrap.fill(text, width)
        image = Image.open('asset/clippy.jpg')
        font = ImageFont.truetype('asset/clippy.ttf', 12)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(12, 12), text=newtext, fill='rgb(0,0,0)', font=font)
        image.save('asset/clippynew.jpg')
        await ctx.send(file=discord.File(fp='asset/clippynew.jpg'))
        os.remove('asset/clippynew.jpg')
    @commands.command()
    async def clippyoption(self, ctx, *, text : str = None):
        if text == None:
            NothingArray = [
                "Clippy says: *Please provide some text!*",
                "Clippy says: *Input some arguments!*",
                "Input some text for clippy!",
                "Please provide text for clippy!"
            ]
            await ctx.send(random.choice(NothingArray))
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
    @commands.command()
    async def clippyok(self, ctx, *, text : str = None):
        if text == None:
            NothingArray = [
                "Clippy says: *Please provide some text!*",
                "Clippy says: *Input some arguments!*",
                "Input some text for clippy!",
                "Please provide text for clippy!"
            ]
            await ctx.send(random.choice(NothingArray))
            return
        width = 36
        newtext = textwrap.fill(text, width)
        image = Image.open('asset/clippy_ok.jpg')
        font = ImageFont.truetype('asset/clippy.ttf', 29)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(34, 45), text=newtext, fill='rgb(0,0,0)', font=font)
        image.save('asset/clippyoknew.jpg')
        await ctx.send(file=discord.File(fp='asset/clippyoknew.jpg'))
        os.remove('asset/clippyoknew.jpg')
def setup(bot):
    bot.add_cog(clippy(bot))
