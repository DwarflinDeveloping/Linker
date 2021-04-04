import discord


async def send_usage_help(ctx):
    help_embed = discord.Embed(
        title=
        "Usage help",
        description=
        "**The principle:**\n"
        "This bot makes it easier to generate links to some keywords.\n"
        "By bracketing a word with `{` and `}`, the bot automatically "
        "generates a link from the URL specified by the guild.\n"
        "If the guild does not have a Custom URL, the URL specified by the user will be used.\n\n"
        "You can find detailed instructions with pictures [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)"
    )

    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=help_embed)


async def send_op_command_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"op\"",
        description=
        "**Variants:**\n"
        " • `%op get` – Outputs a list of the operators\n"
        " • `%op add <user id>` – Adds operator rights to the user\n"
        " • `%op remove <user id>` – Removes operator rights to the user\n\n"
        "**Use:**\n"
        "With this command you can query and manage the operators.\n"
        "To run it you need at least `administrator` permissions in the bot system.\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_guildfamily_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"guildfamily\"",
        description=
        "**Variants:**\n"
        " • `%guildfamily get` – Outputs the guilds default url\n"
        " • `%guildfamily set <url>` – Sets the guilds default url\n\n"
        "**Use:**\n"
        "With this command you can query and manage the Default URL of the guild.\n"
        "To run it you need `manage_messages` permission in the current channel.\n"
        "We therefore recommend creating a channel for bot commands so that the system works properly.\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_userfamily_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"userfamily\"",
        description=
        "**Variants:**\n"
        " • `%userfamily get` – Outputs your default url\n"
        " • `%userfamily set <url>` – Sets your default url\n\n"
        "**Use:**\n"
        "With this command you can query and manage your Default URL\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_userwords_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"userwords\"",
        description=
        "**Variants:**\n"
        " • `%userwords list` – Outputs your custom words\n"
        " • `%userwords set <word> <url>` – Sets your custom words\n\n"
        "**Use:**\n"
        "With this command you can query and manage your custom words.\n\n"
        "_Custom Words_ are words that every user and guild has. "
        "When this word is searched in curly brackets, no URL is generated, "
        "but the Custom URL assigned to the word.\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_guildwords_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"guildwords\"",
        description=
        "**Variants:**\n"
        " • `%guildwords list` – Outputs your custom words\n"
        " • `%guildwords set <word> <url>` – Sets your custom words\n\n"
        "**Use:**\n"
        "With this command you can query and manage the guilds custom words.\n\n"
        "_Custom Words_ are words that every user and guild has. "
        "When this word is searched in curly braces, no URL is generated, "
        "but the Custom URL assigned to the word.\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_default_url_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"default url\"",
        description=
        "**Explanation:**\n"
        "A _Default URL_ is a url that every user and guild has. "
        "When searching for a word in curly braces, the URL is generated from the Default URL set for the guild.\n"
        "If none is specified for the guild, the URL is generated from the user's Default URL.\n\n"
        "**Usage:**\n"
        "`%help userfamily`\n"
        "`%help guildfamily`\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_custom_words_help(ctx):
    help_embed = discord.Embed(
        title=
        f"Help for \"custom words\"",
        description=
        "**Explanation:**\n"
        "_Custom Words_ are words that every user and guild has. "
        "When this word is searched in curly brackets, no URL is generated, "
        "but the Custom URL assigned to the word.\n\n"
        "**Usage:**\n"
        "`%help guildwords`\n"
        "`%help userwords`\n\n"
        "Further questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_help_overview(ctx):
    help_embed = discord.Embed(
        title=
        "Help overview",
        description=
        "**commands:**\n"
        "`%help guildfamily` – Provides help on the \"%guildfamily\" command\n"
        "`%help userfamily` – Provides help on the \"%userfamily\" command\n"
        "`%help guildwords` – Provides help on the \"%guildwords\" command\n"
        "`%help userwords` – Provides help on the \"%userwords\" command\n"
        "`%help usage` – Provides help on using the bot\n\n"
        "**terms:**\n"
        "`%help custom words` – Provides help about custom words\n"
        "`%help default url` – Provides help about default URLs\n\n"
        "A detailed usage guide with pictures can be found [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)."
    )
    help_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def manage_request(ctx, *args):
    args = [arg.lower() for arg in args]
    if len(args) == 0:
        await send_help_overview(ctx)
    elif args[0] == "guildfamily":
        await send_guildfamily_help(ctx)
    elif args[0] == "userfamily":
        await send_userfamily_help(ctx)
    elif args[0] == "usage":
        await send_usage_help(ctx)
    elif args[0] == "guildwords":
        await send_guildwords_help(ctx)
    elif args[0] == "userwords":
        await send_userwords_help(ctx,)
    elif args[0] == "customwords" or args[0] == "custom" and args[1] == "words":
        await send_custom_words_help(ctx)
    elif args[0] == "defaulturl" or args[0] == "default" and args[1] == "url":
        await send_default_url_help(ctx)
    elif args[0] == "op":
        from commands.admincmds import operators
        if ctx.author.id not in operators:
            from embeds import create_custom_embed
            from discord import Colour
            await ctx.send(
                embed=create_custom_embed(
                    embed_message=
                    "You are not permitted to use this command.\n"
                    "To execute this command you must have `administrator` rights",
                    user=ctx.author,
                    colour=Colour.dark_red()
                )
            )
            return
        await send_op_command_help(ctx)
    else:
        from embeds import create_custom_embed
        from discord import Colour
        await ctx.send(
            embed=create_custom_embed(
                embed_message=
                "Unfortunately, this help article does not exist.\n"
                "For a list of currently existing help articles, see `%help`.",
                user=ctx.author,
                colour=Colour.dark_red()
            )
        )
