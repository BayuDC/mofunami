from discord import Embed
from discord.ext import commands, tasks
from core import loop_errors
from core.loop import Loop


class Utility(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    # ? TODO
    # * check before invoke
    # * infinity loop
    # * stop loop command
    @commands.command()
    async def loop(self, ctx: commands.Context, *args):
        if not args:
            raise loop_errors.MissingRequiredArgument

        # * create loop object
        loop = Loop(args)

        # * prepare command for loop
        command: commands.Command = self.bot.get_command(loop.command)
        if command is None:
            raise loop_errors.CommandNotFound
        if command.name == ctx.command.name:
            raise loop_errors.CommandProhibited

        # * create loop task
        @tasks.loop(seconds=loop.interval, count=loop.count)
        async def action():
            await ctx.invoke(command, *loop.args)

        # * send success message
        embed = Embed(title='Loop created successfully')

        embed.add_field(name='Command', value=f"`{command.name}{loop.pretty_args()}`", inline=False)
        embed.add_field(name='Interval', value=loop.pretty_time(), inline=False)
        embed.add_field(name='Count', value=f"`{loop.count}`", inline=False)

        await ctx.send(embed=embed)

        # * start loop
        action.start()

    @loop.error
    async def loop_error(self, ctx, error):
        try:
            raise error
        except loop_errors.MissingRequiredArgument:
            await ctx.send("I can't loop nothing")
        except loop_errors.CommandNotFound:
            await ctx.send('Please input a valid command for loop')
        except loop_errors.CommandProhibited:
            await ctx.send(f"Can't loop command `{ctx.command.name}`")
        except:
            await ctx.send('Something went wrong')


def setup(bot):
    bot.add_cog(Utility(bot))
