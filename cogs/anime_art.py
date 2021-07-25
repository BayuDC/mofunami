import nekos

from discord.ext import commands
from data.nekos_life import categories


class AnimeArt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['nekos-life'])
    async def nekos(self, ctx, category):
        if not category:
            return await ctx.send('Please enter a specific category')
        if category not in categories:
            return await ctx.send('Categories not found!')

        await ctx.send(nekos.img(category))


def setup(bot):
    bot.add_cog(AnimeArt(bot))
