import requests as req

from discord import Embed
from discord.ext import commands
from urllib.parse import quote


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx: commands.Context, country: str = ''):
        country_esc = quote(country, safe='')
        base_url = 'https://covid19.mathdro.id/api'
        res: req.Response = req.get(base_url if not country else f'{base_url}/countries/{country_esc}')

        if res.ok:
            covid = res.json()

            embed = Embed(
                title=f"Covid-19 Situation in {'Worldwide' if not country else country}",
                description='To see Covid-19 data by country use `.covid <country>`' if not country else 'To see Covid-19 data in worldwide use `.covid`',
            )
            embed.add_field(name='Confirmed', value=covid['confirmed']['value'])
            embed.add_field(name='Recovered', value=covid['recovered']['value'])
            embed.add_field(name='Deaths', value=covid['deaths']['value'])
            embed.set_footer(text=f"Last update: {covid['lastUpdate'].replace('T', ' ')}")

            return await ctx.send(embed=embed)

        if country:
            return await ctx.send(res.json()['error']['message'])
        await ctx.send('Oops, Something went wrong!')


def setup(bot):
    bot.add_cog(Info(bot))
