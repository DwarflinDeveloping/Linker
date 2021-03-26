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
        f"Help for \"{args[0]}\"",
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


async def send_help_overview(ctx):
    help_embed = discord.Embed(
        title=
        "Help overview",
        description=
        "**help articles:**\n"
        "`%help guildfamily` – Provides help on the \"%guildfamily\" command\n"
        "`%help userfamily` – Provides help on the \"%userfamily\" command\n"
        "`%help usage` – Gives help on using the bot"
    )

    help_embed.set_footer(text=f"Request of {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=help_embed)


async def manage_request(ctx, *args):
    if len(args) == 0:
        await send_help_overview(ctx)
    elif args[0] == "guildfamily":
        await send_guildfamily_help(ctx, *args)
    elif args[0] == "userfamily":
        await send_userfamily_help(ctx, *args)
    elif args[0] == "usage":
        await send_usage_help(ctx)
    else:
        await ctx.send("I am sorry, but i could not find this article. :(")
