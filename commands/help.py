import discord


async def send_usage_help(ctx):
    help_embed = discord.Embed(
        title=
        "Usage help",
        description=
        "**The principle:**\n"
        "This bot makes it possible to send links much faster.\n"
        "By bracketing a word with `{` and `}`, the bot automatically "
        "generates a link from the URL specified by the guild.\n"
        "If the guild does not have a specified URL, the URL specified by the user will be used.\n\n"
        "You can find detailed instructions with pictures [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)"
    )

    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=help_embed)


async def send_guildfamily_help(ctx, *args):
    help_embed = discord.Embed(
        title=
        f"Help for \"{args[0]}\"",
        description=
        "**Variants:**\n"
        " • `%guildfamily get` – Outputs the guilds default url\n"
        " • `%guildfamily set <url>` – Sets the guilds default url\n\n"
        "**Use:**\n"
        "With this command you can change the default url of the guild.\n"
        "To run it you need `manage_messages` permission in the current channel.\n"
        "We therefore recommend creating a channel for bot commands so that the system works properly.\n\n"
        "Still unanswered questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_userfamily_help(ctx, *args):
    help_embed = discord.Embed(
        title=
        f"Help for \"userfamily\"",
        description=
        "**Variants:**\n"
        " • `%userfamily get` – Outputs your default url\n"
        " • `%userfamily set <url>` – Sets your default url\n\n"
        "**Use:**\n"
        "With this command you can output and manage your default url\n\n"
        "Still unanswered questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_userwords_help(ctx, *args):
    help_embed = discord.Embed(
        title=
        f"Help for \"userwords\"",
        description=
        "**Variants:**\n"
        " • `%userwords list` – Outputs your custom words\n"
        " • `%userwords set <word> <url>` – Sets your custom words\n\n"
        "**Use:**\n"
        "With this command you can output and manage your custom words.\n\n"
        "_Custom Words_ are words that every user and guild has. "
        "When this word is searched in curly brackets, no URL is generated, "
        "but the Custom URL assigned to the word.\n\n"
        "Still unanswered questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_guildwords_help(ctx, *args):
    help_embed = discord.Embed(
        title=
        f"Help for \"guildwords\"",
        description=
        "**Variants:**\n"
        " • `%guildwords list` – Outputs your custom words\n"
        " • `%guildwords set <word> <url>` – Sets your custom words\n\n"
        "**Use:**\n"
        "With this command you can output and manage the guilds custom words.\n\n"
        "_Custom Words_ are words that every user and guild has. "
        "When this word is searched in curly braces, no URL is generated, "
        "but the Custom URL assigned to the word.\n\n"
        "Still unanswered questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_default_url_help(ctx, *args):
    help_embed = discord.Embed(
        title=
        f"Help for \"custom words\"",
        description=
        "**Explanation:**\n"
        "A _Default URL_ is a utl that every user and guild has. "
        "When searching for a word in curly braces, the URL is generated from the Default URL set for the guild.\n"
        "If none is specified for the guild, the URL is generated from the user's Default URL.\n\n"
        "**Usage:**\n"
        "`%help userfamily`\n"
        "`%help guildfamily`\n\n"
        "Still unanswered questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def send_custom_words_help(ctx, *args):
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
        "Still unanswered questions? You can find help [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)!"
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)
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
        "`%help usage` – Gives help on using the bot\n\n"
        "**terms:**\n"
        "`%help custom words` – Provides help about custom words\n"
        "`%help default url` – Provides help about default URLs\n\n"
        "A detailed usage guide with pictures can be found [here]"
        "(https://github.com/DwarflinDeveloping/Linker/blob/main/README.md)."
    )
    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=help_embed)

    from utils import ReturnCodes
    return ReturnCodes.SUCCESS


async def manage_request(ctx, *args):
    args = [arg.lower() for arg in args]
    if len(args) == 0:
        await send_help_overview(ctx)
    elif args[0] == "guildfamily":
        await send_guildfamily_help(ctx, *args)
    elif args[0] == "userfamily":
        await send_userfamily_help(ctx, *args)
    elif args[0] == "usage":
        await send_usage_help(ctx)
    elif args[0] == "guildwords":
        await send_guildwords_help(ctx, *args)
    elif args[0] == "userwords":
        await send_userwords_help(ctx, *args)
    elif args[0] == "customwords" or args[0] == "custom" and args[1] == "words":
        await send_custom_words_help(ctx, *args)
    elif args[0] == "defaulturl" or args[0] == "default" and args[1] == "url":
        await send_default_url_help(ctx, *args)
    else:
        await ctx.send("Unfortunately, this help article does not exist.\n"
                       "For a list of currently existing help articles, see `%help`.")
