from discord.ext import commands
extensions = [
    "Cogs.Fun.gift",
    "Cogs.Fun.time",
    "Cogs.Util.ping",
    "Cogs.Fun.boop",
    "Cogs.help",
    "Cogs.Fun.hug",
    "Cogs.Fun.button",
    "Cogs.Fun.clippy",
    "Cogs.Admin",
    "Cogs.Fun.Music.Music",
    "Cogs.Util.wikipedia"
]
bot = commands.Bot(command_prefix="$", case_insensitive=False)
bot.remove_command('help')
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f"[=Loaded=]: {extension}")
        except Exception as error:
            print(f"[=Error=] {error}")
bot.run("NTY4NTIxMTY4NTA0NjE5MDI4.XMkCKA.c5VEPvAVSwC2TPhzRshcW8VdTHk")