from discord.ext import commands, tasks
from discord.ext.commands.errors import BadArgument, CommandNotFound


class Utility(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def loop(self, ctx: commands.Context, *args):
        if len(args) == 0:
            raise BadArgument

        interval = count = command = None

        if args[0].isdigit():
            interval, *args = args
            interval = int(interval)

        if args[0].isdigit():
            count, *args = args
            count = int(count)

        command, *args = args

        interval = interval or 1
        count = count or 10
        command = self.bot.get_command(command)

        if command is None:
            raise CommandNotFound

        @tasks.loop(seconds=interval, count=count)
        async def action():
            await ctx.invoke(command, *args)

        action.start()

    @loop.error
    async def loop_error(self, ctx, error):
        try:
            raise error
        except CommandNotFound:
            await ctx.send("Can not start loop")
        except BadArgument:
            await ctx.send("Argument `command` is required")


def setup(bot):
    bot.add_cog(Utility(bot))
