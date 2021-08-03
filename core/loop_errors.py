from discord.ext.commands import errors


class CommandNotFound(errors.CommandError):
    pass


class MissingRequiredArgument(errors.UserInputError):
    pass


class CommandProhibited(errors.CommandError):
    pass
