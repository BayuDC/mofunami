import os

from discord.ext import commands
from config import prefix as bot_prefix

token = os.getenv('BOT_TOKEN')
prefix = os.getenv('BOT_PREFIX') or bot_prefix
bot = commands.Bot(prefix)

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
