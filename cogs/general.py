from discord.ext import commands
from config import prefix


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def say(self, ctx: commands.Context):
        msg = ctx.message
        text = msg.content.replace(f'{prefix}say', '', 1)

        try:
            await msg.delete()
        finally:
            await ctx.send(text)


def setup(bot):
    bot.add_cog(General(bot))
