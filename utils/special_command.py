from discord.enums import ChannelType

guilds = [859079215574810674]
users = [704845945325748354]


class SpecialCommand:
    def check(self, ctx):
        if ctx.channel.type == ChannelType.private:
            return ctx.author.id in users

        return ctx.guild.id in guilds

    async def error(self, ctx):
        await ctx.send(f'Sorry, command `{ctx.command.name}` is not available for now')


special = SpecialCommand()
