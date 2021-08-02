import os

from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from config import prefix, token

if not token:
    print('Bot token not found')
    exit()

bot = commands.Bot(prefix)


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return await ctx.send('Command not found')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename.replace('.py', '')}")

bot.run(token)
