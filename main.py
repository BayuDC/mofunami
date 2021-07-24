import os

from discord.ext import commands
from config import prefix

bot = commands.Bot(prefix)
token = os.getenv('BOT_TOKEN')

if not token:
    print('Bot token not found')
    exit()


@bot.event
async def on_ready():
    print('Bot is ready')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename.replace('.py', '')}")

bot.run(token)
