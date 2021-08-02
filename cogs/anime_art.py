from discord import Embed
from discord.ext import commands
from discord.ext.commands import errors

from core import nekos as nekos_core
from utils import special_command
from config import prefix


class AnimeArt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check(special_command.check)
    @commands.command(aliases=['nekos-life'])
    async def nekos(self, ctx: commands.Context, category):
        img = nekos_core.img(category)

        if img is None:
            return await ctx.send('Category not found!')

        return await ctx.send(img)

    @nekos.error
    async def nekos_error(self, ctx: commands.Context, error):
        try:
            raise error
        except errors.CheckFailure:
            await special_command.error(ctx)
        except errors.MissingRequiredArgument:
            category = nekos_core.category_random()
            img = nekos_core.img('nsfw_avatar')

            embed = Embed(title='Please enter a specific category')
            embed.set_author(name='Nekos-Life', icon_url=img)
            embed.set_thumbnail(url=img)

            embed.add_field(name='Available Categories', value=nekos_core.category_summary(), inline=False)
            embed.add_field(name='Usage', value=f'`{prefix}{ctx.command.name} <category>`')
            embed.add_field(name='Example', value=f'`{prefix}{ctx.command.name} {category}`')

            await ctx.send(embed=embed)
            pass
        except:
            await ctx.send('Something went wrong')


def setup(bot):
    bot.add_cog(AnimeArt(bot))
