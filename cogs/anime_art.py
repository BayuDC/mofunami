import nekos

from discord.ext import commands
from discord.ext.commands.errors import CheckFailure
from data.nekos_life import categories
from utils.special_command import special


class AnimeArt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check(special.check)
    @commands.command(aliases=['nekos-life'])
    async def nekos(self, ctx, category):
        if not category:
            return await ctx.send('Please enter a specific category')
        if category not in categories:
            return await ctx.send('Categories not found!')

        await ctx.send(nekos.img(category))

    @nekos.error
    async def nekos_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            return await special.error(ctx)

        raise error


def setup(bot):
    bot.add_cog(AnimeArt(bot))
