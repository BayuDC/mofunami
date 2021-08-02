from discord.ext import commands
from discord.ext.commands import errors


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def say(self, ctx: commands.Context, *args):
        if not args:
            return await ctx.send("I can't say nothing")

        text = ' '.join(args)

        try:
            if ctx.invoked_with == 'say':
                await ctx.message.delete()
        except errors.CommandInvokeError:
            pass
        finally:
            await ctx.send(text)


def setup(bot):
    bot.add_cog(General(bot))
