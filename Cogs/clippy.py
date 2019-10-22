import os
import random
import textwrap

import discord
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from discord.ext import commands


class clippy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clippy(self, ctx, *, text : str = None):
        '''Generates a clippy image with your desired text.'''
        if text == None:
            NothingList = [
                "Clippy says: *Please provide some text!*",
                "Clippy says: *Input some arguments!*",
                "Input some text for clippy!",
                "Please provide text for clippy!"
            ]
            await ctx.send(random.choice(NothingList))
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

def setup(bot):
    bot.add_cog(clippy(bot))
