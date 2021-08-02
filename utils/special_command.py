from discord.enums import ChannelType

guilds = [859079215574810674]
users = [704845945325748354]

def check(ctx):
    if ctx.channel.type == ChannelType.private:
        return ctx.author.id in users

    return ctx.guild.id in guilds

async def error(ctx):
    await ctx.send(f'Sorry, command `{ctx.command.name}` is not available for now')


