import os

from discord.ext import commands
from config import token, prefix

bot = commands.Bot(prefix)


@bot.event
async def on_ready():
    print('Bot is ready')

for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        bot.load_extension(f"cogs.{filename.replace('.py', '')}")

bot.run(token)
