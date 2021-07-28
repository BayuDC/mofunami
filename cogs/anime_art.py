from discord import Embed
from discord.ext import commands
from discord.ext.commands.errors import CheckFailure, MissingRequiredArgument
from utils.special_command import special
from core.nekos_life import nekos_core
from config import prefix


class AnimeArt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check(special.check)
    @commands.command(aliases=['nekos-life'])
    async def nekos(self, ctx, category):
        img_url = nekos_core.get_img(category)

        if img_url is None:
            return await ctx.send('Category not found!')

        return await ctx.send(img_url)

    @nekos.error
    async def nekos_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            return await special.error(ctx)
        if isinstance(error, MissingRequiredArgument):
            category = nekos_core.get_category()
            img_url = nekos_core.get_img('nsfw_avatar')

            embed = Embed(title='Please enter a specific category')
            embed.set_author(name='Nekos-Life', icon_url=img_url)
            embed.set_thumbnail(url=img_url)

            embed.add_field(name='Available Categories', value=nekos_core.get_categories(), inline=False)
            embed.add_field(name='Usage', value=f'`{prefix}{ctx.command.name} <category>`')
            embed.add_field(name='Example', value=f'`{prefix}{ctx.command.name} {category}`')

            return await ctx.send(embed=embed)

        raise error


def setup(bot):
    bot.add_cog(AnimeArt(bot))
