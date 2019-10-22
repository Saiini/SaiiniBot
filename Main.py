from discord.ext import commands
extensions = [
    "Cogs.gift",
    "Cogs.time",
    "Cogs.ping",
    "Cogs.boop",
    "Cogs.help",
    "Cogs.hug",
    "Cogs.button",
    "Cogs.Admin",
    "Cogs.wikipedia",
    "Cogs.halloween",
    "Cogs.car_rhymes"
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
bot.run("NTk0Mzg5NzAzNjM4Mzg0NjUw.Xa506w.YJ-vO1SCGwmU8BDbD8XzwvdCmC8")
